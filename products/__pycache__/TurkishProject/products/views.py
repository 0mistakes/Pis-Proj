from django.shortcuts import render, redirect, get_object_or_404

from datetime import datetime
from products.models import ApartCategory, Apart, TypeOfApart, ApartPlan, Vidovaya, Mebel, LcdOrSingle

def index(request):
    categories = ApartCategory.objects.all()
    cities = Apart.objects.values_list('city', flat=True).distinct()
    context = {
        'title': 'Store',
        'categories': categories,
        'cities': cities,
    }
    return render(request, 'products/index.html' ,context)


def search(request):
    category_id = request.GET.get('category_id') or request.GET.get('category_id', None)
    type_id = request.GET.get('type_id')
    start_year = request.GET.get('start_year')
    end_year = request.GET.get('end_year')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    mebel_ids = request.GET.getlist('mebel')
    vidovaya = request.GET.get('vidovaya')
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
    selected_category_id = request.GET.get('category_id')

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

    if developer:
        products = products.filter(developer=developer)

    if min_price is None:
        min_price = 0

    if max_price is None:
        max_price = 50000000

    if min_price and max_price:
        products = products.filter(price__gte=float(min_price), price__lte=float(max_price))

    if start_year and end_year:
        products = products.filter(buildingAge__gte=int(start_year), buildingAge__lte=int(end_year))

    if start_floor and end_floor:
        products = products.filter(qauntityOfFloors__gte=int(start_floor), qauntityOfFloors__lte=int(end_floor))

    if start_metres and end_metres:
        products = products.filter(quantityOfMetres__gte=int(start_metres), quantityOfMetres__lte=int(end_metres))

    if category_id:
        selected_category_ids = [int(id) for id in category_id.split(',')]
        products = products.filter(category__id__in=selected_category_ids)

    if type_id:
        type_of_apart = TypeOfApart.objects.get(id=type_id)
        products = products.filter(typeOfApart=type_of_apart)

    if mebel_ids:
        products = products.filter(mebel__in=mebel_ids)

    if vidovaya:
        products = products.filter(vidovaya_id=int(vidovaya))

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
        # Очистить параметры фильтрации
        return redirect('search')

    num_results = products.count()

    context = {
        'title': 'Store - Buying',
        'products': products,
        'categories': categories,
        'typeOfAparts': type_of_aparts,
        'num_results': num_results,
        'min_price': min_price,
        'max_price': max_price,
        'mebels': mebels,
        'vidovayas': vidovayas,
        'lcdorsingles': lcdorsingles,
        'apartPlans' : apartPlans,
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
        'selected_category_id': selected_category_id,
    }

    return render(request, 'products/search.html', context)



def search_by_year(request):
    return search(request)

def search_by_category(request, category_id):
    return search(request, category_id=category_id)


def search_by_type(request, type_id):
    return search(request, type_id=type_id)


def about_us(request):
    return render(request, 'products/about_us.html')

def tovar(request):
    apart_id = request.GET.get('id')
    apart = get_object_or_404(Apart, id=apart_id)
    return render(request, 'products/tovar.html', {'apart': apart})




