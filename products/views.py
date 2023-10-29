from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
import locale
from math import ceil
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from datetime import datetime
import requests
from products.models import ApartCategory, Apart, TypeOfApart, ApartPlan, Vidovaya, Mebel, LcdOrSingle


def index(request):
    categories = ApartCategory.objects.all()
    cities = Apart.objects.values_list('city', flat=True).distinct()
    apartments = Apart.objects.all()

    context = {
        'title': 'Store',
        'categories': categories,
        'cities': cities,  # Передаем выбранную категорию в контекст
        'apartments': apartments,
    }
    return render(request, 'products/index.html', context)


def search(request):
    apart_id = request.GET.get('id') or request.POST.get('id')
    category_id = request.GET.get('category_id')
    type_id = request.GET.get('type_id')
    start_year = request.GET.get('start_year')
    end_year = request.GET.get('end_year')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    mebel_ids = request.GET.getlist('mebel')
    vidovaya = request.GET.getlist('vidovaya')
    lcdorsingle = request.GET.getlist('lcdorsingle')
    apartPlan = request.GET.getlist('apartPlan')
    quantity_room = request.GET.get('quantityRoom')
    developer = request.GET.get('developer')
    infostracture = request.GET.get('infostracture')
    start_floor = request.GET.get('start_floor')
    end_floor = request.GET.get('end_floor')
    start_metres = request.GET.get('start_metres')
    end_metres = request.GET.get('end_metres')
    selected_bathroom = request.GET.get('quantityOfBathroom')
    category_name = request.GET.get('category_name')
    city = request.GET.get('city')
    price_order = request.GET.get('price_order')

    quantity_rooms = Apart.objects.values_list('quantityRoom', flat=True).distinct()
    products = Apart.objects.all()
    type_of_aparts = TypeOfApart.objects.all()
    categories = ApartCategory.objects.all()
    mebels = Mebel.objects.all()
    vidovayas = Vidovaya.objects.all()
    lcdorsingles = LcdOrSingle.objects.all()
    apartPlans = ApartPlan.objects.all()
    all_aparts = Apart.objects.all()
    apartment_numbers = Apart.objects.values_list('apartmentNumber', flat=True).distinct()
    selected_apartment_number = request.GET.get('apartment_number')
    bathroom_counts = Apart.objects.values('quantityOfBathroom').distinct()

    current_year = datetime.now().year

    building_ages = [current_year - apart.buildingAge for apart in all_aparts]
    category_ids = []
    for category in categories:
        category_id = request.GET.get('category_id_{}'.format(category.id))
        if category_id:
            category_ids.append(category_id)

    if category_ids:
        products = products.filter(category__in=category_ids)

    if category_name:
        products = products.filter(category__name=category_name)

    if city:
        products = products.filter(city=city)

    if price_order == 'desc':
        products = products.order_by('-price')
    elif price_order == 'asc':
        products = products.order_by('price')

    if type_id:
        type_of_apart = TypeOfApart.objects.get(id=type_id)
        products = products.filter(typeOfApart=type_of_apart)

    if developer:
        products = products.filter(developer=developer)

    if min_price is None:
        min_price = 0

    if max_price is None:
        max_price = 50000000

    if min_price and max_price:
        products = products.filter(price__gte=float(min_price), price__lte=float(max_price))

    if start_year:
        start_year = int(start_year)
        products = products.filter(buildingAge__gte=start_year)

    if end_year:
        end_year = int(end_year)
        products = products.filter(buildingAge__lte=end_year)

    if start_year and end_year:
        products = products.filter(buildingAge__gte=int(start_year), buildingAge__lte=int(end_year))

    if start_floor and end_floor:
        products = products.filter(qauntityOfFloors__gte=int(start_floor), qauntityOfFloors__lte=int(end_floor))

    if start_metres and end_metres:
        products = products.filter(quantityOfMetres__gte=int(start_metres), quantityOfMetres__lte=int(end_metres))

    if mebel_ids:
        products = products.filter(mebel__in=mebel_ids)

    if vidovaya:
        products = products.filter(vidovaya__in=vidovaya)

    if lcdorsingle:
        products = products.filter(LcdOrS__in=lcdorsingle)

    if apartPlan:
        products = products.filter(apartPlan__in=apartPlan)

    if quantity_room:
        products = products.filter(quantityRoom=quantity_room)

    if infostracture == '1':
        products = products.exclude(infostracture=None)
    elif infostracture == '2':
        products = products.filter(infostracture=None)

    if 'reset_filters' in request.GET:
        return redirect('search')

    page = request.GET.get("page", 1)

    products_per_page = 12
    paginator = Paginator(products, products_per_page)

    try:
        paginated_products = paginator.page(page)
    except PageNotAnInteger:
        paginated_products = paginator.page(1)
    except EmptyPage:
        paginated_products = paginator.page(paginator.num_pages)

    num_results = products.count()
    context = {
        'title': 'Store - Buying',
        'products': paginated_products,
        'categories': categories,
        'typeOfAparts': type_of_aparts,
        'num_results': num_results,
        'min_price': min_price,
        'max_price': max_price,
        'mebels': mebels,
        'vidovayas': vidovayas,
        'lcdorsingles': lcdorsingles,
        'apartPlans': apartPlans,
        'quantityRooms': quantity_rooms,
        'selected_quantity_room': quantity_room,
        'selected_developer': developer,
        'building_ages': building_ages,
        'start_floor': start_floor,
        'end_floor': end_floor,
        'start_year': start_year,
        'end_year': end_year,
        'infostracture': infostracture,
        'start_metres': start_metres,
        'end_metres': end_metres,
        'apartment_numbers': apartment_numbers,
        'selected_apartment_number': selected_apartment_number,
        'bathroom_counts': bathroom_counts,
        'paginator': paginator,
        'page_obj': paginated_products,
    }

    if paginated_products.has_next():
        remaining_products = paginator.get_page(paginated_products.next_page_number())
        context['remaining_products'] = remaining_products

    return render(request, 'products/search.html', context)




def search_by_year(request):
    return search(request)

def search_by_category(request, category_id):
    return search(request, category_id=category_id)


def search_by_type(request, type_id):
    return search(request, type_id=type_id)


def about_us(request):
    return render(request, 'products/about_us.html')

def contact_us(request):
    return render(request, 'products/contact_us.html')

def buying_in_Kipr(request):
    return render(request, 'products/Byuing_In_Kipr.html')

def buying_in_Turk(request):
    return render(request, 'products/Buying_In_Turkish.html')

def health(request):
    return render(request, 'products/health.html')

def how_are_we(request):
    return render(request, 'products/how_are_we.html')

def rasxodi(request):
    return render(request, 'products/rasxodi.html')

def Turkish_citezenship(request):
    return render(request, 'products/Turkish_citizenship.html')

def VidNaShitelstvo(request):
    return render(request, 'products/VidNaShitelstvo.html')

def why_turk(request):
    return render(request, 'products/Why_Turkish.html.')

def procedure(request):
    return render(request, 'products/Процедура покупки.html')

def tapu(request):
    return render(request, 'products/ТАПУ.html')

def fondi(request):
    return render(request, 'products/Фонды недвижимости.html')

def trusting(request):
    return render(request, 'products/Trusting.html')






def tovar(request):
    if request.method == 'POST':
        is_lead_form = request.POST.get('is_lead_form') == 'true'

        if is_lead_form:
            # Обработка формы создания лида
            name1 = request.POST.get('name1')
            phone1 = request.POST.get('phone1')
            email1 = request.POST.get('email1')
            contact_method = request.POST.get('contact-method')
            apart_name = request.POST.get('apart-name')
            apart_price = request.POST.get('apart-price')

            # Создание лида в Bitrix24
            lead_data = {
                'fields': {
                    'TITLE': apart_name,
                    'NAME': name1,
                    'PHONE': [{'VALUE': phone1, 'VALUE_TYPE': 'WORK'}],
                    'EMAIL': [{'VALUE': email1, 'VALUE_TYPE': 'WORK'}],
                    'IM': [{'VALUE': contact_method, 'VALUE_TYPE': 'WORK'}],
                    'OPPORTUNITY': apart_price,
                },
            }

            url = 'https://b24-1dk1va.bitrix24.ru/rest/1/28ck3wiw97e5ztfz/crm.lead.add.json'
            response = requests.post(url, json=lead_data)

            if response.status_code == 200:
                # Лид успешно создан
                apart_id = request.GET.get('id') or request.POST.get('id')
                apart = get_object_or_404(Apart, id=apart_id)
                similar_aparts = Apart.objects.exclude(id=apart_id)[:3]
                apart_price = int(apart.price)
                apart_price_formatted = '{:,}'.format(apart_price).replace(',', ' ')
                euro_price = apart.price / 98
                euro_price = int(euro_price)
                euro_price = '{:,}'.format(euro_price).replace(',', ' ')
                lir_price = apart.price / 3.5
                lir_price = int(lir_price)
                lir_price = '{:,}'.format(lir_price).replace(',', ' ')
                context = {
                    'euro_price': euro_price,
                    'lir_price': lir_price,
                    'apart_price_formatted': apart_price_formatted,
                    'apart': apart,
                    'success_message': True,
                    'similar_aparts': similar_aparts,
                }
                return render(request, 'products/tovar.html', context)
            else:
                apart_id = request.GET.get('id') or request.POST.get('id')
                apart = get_object_or_404(Apart, id=apart_id)
                similar_aparts = Apart.objects.exclude(id=apart_id)[:3]
                apart_price = int(apart.price)
                apart_price_formatted = '{:,}'.format(apart_price).replace(',', ' ')
                euro_price = apart.price / 98
                euro_price = int(euro_price)
                euro_price = '{:,}'.format(euro_price).replace(',', ' ')
                lir_price = apart.price / 3.5
                lir_price = int(lir_price)
                lir_price = '{:,}'.format(lir_price).replace(',', ' ')
                context = {
                    'euro_price': euro_price,
                    'lir_price': lir_price,
                    'apart_price_formatted': apart_price_formatted,
                    'apart': apart,
                    'success_message': True,
                    'similar_aparts': similar_aparts,
                }
                return render(request, 'products/tovar.html', context)

        else:
            # Обработка формы отправки простого сообщения на почту
            name = request.POST.get('name')
            phone = request.POST.get('phone')

            # Отправка письма
            subject = 'Новая заявка'
            message = f'Имя: {name}\nТелефон: {phone}'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = 'shtorm05045@yandex.com'
            send_mail(subject, message, from_email, [to_email])

            # Возврат успешного сообщения или другой логики
            return render(request, 'products/tovar.html', {'success_message': True})

    # Если нет POST запроса, отображаем страницу с формами
    apart_id = request.GET.get('id') or request.POST.get('id')
    apart = get_object_or_404(Apart, id=apart_id)

    apart_price = int(apart.price)
    apart_price_formatted = '{:,}'.format(apart_price).replace(',', ' ')
    euro_price = apart.price / 98
    euro_price = int(euro_price)
    euro_price = '{:,}'.format(euro_price).replace(',', ' ')
    lir_price = apart.price / 3.5
    lir_price = int(lir_price)
    lir_price = '{:,}'.format(lir_price).replace(',', ' ')
    similar_aparts = Apart.objects.exclude(id=apart_id)[:3]

    # Проверяем, был ли передан параметр 'show_more' в запросе
    show_more = request.GET.get('show_more')

    if show_more:
        # Обработка клика на дополнительные результаты
        # Здесь вы можете выполнить логику, связанную с отображением страницы с дополнительными товарами
        # Например, загрузить дополнительные товары и передать их в контекст шаблона
        additional_aparts = Apart.objects.exclude(id=apart_id)[3:6]
        context = {
            'apart': apart,
            'similar_aparts': similar_aparts,
            'additional_aparts': additional_aparts,
            'euro_price': euro_price,
            'lir_price': lir_price,
            'apart_price_formatted': apart_price_formatted,
        }
        return render(request, 'products/tovar.html', context)

    else:
        # Отображение основной страницы с товаром
        context = {
            'apart': apart,
            'similar_aparts': similar_aparts,
            'euro_price' :  euro_price,
            'lir_price': lir_price,
            'apart_price_formatted': apart_price_formatted,
        }
        return render(request, 'products/tovar.html', context)





