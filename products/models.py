from django.db import models
# Create your models here.

class ApartCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'Категория недвижимости'
        verbose_name_plural = 'Категории недвижимости'

    def __str__(self):
        return self.name

class TypeOfApart(models.Model):
    type = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Типы недвижимости'

    def __str__(self):
        return self.type

class Mebel(models.Model):
    type = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'Мебель'
        verbose_name_plural = 'Мебель'

    def __str__(self):
        return self.type

class Vidovaya(models.Model):
    type = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'Видовая характеристика'
        verbose_name_plural = 'Видовые характеристики'

    def __str__(self):
        return self.type

class LcdOrSingle(models.Model):
    type = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'ЖК или одиночное здание'
        verbose_name_plural = 'ЖК или одиночные здания'

    def __str__(self):
        return self.type

class ApartPlan(models.Model):
    type = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'Планировка недвижимости'
        verbose_name_plural = 'Планировки недвижимости'

    def __str__(self):
        return self.type


class Apart(models.Model):
    name = models.CharField(max_length=256, verbose_name=('Название'))
    description = models.TextField(verbose_name=('Описание'))
    price = models.FloatField(verbose_name=('Цена'))
    image = models.ImageField(upload_to='products_images', verbose_name=('Изображение'))
    Tovarimage1 = models.ImageField(upload_to='products_images', null=True, verbose_name=('Изображение товара 1'))
    Tovarimage2 = models.ImageField(upload_to='products_images', null=True, verbose_name=('Изображение товара 2'))
    Tovarimage3 = models.ImageField(upload_to='products_images', null=True, verbose_name=('Изображение товара 3'))
    city = models.TextField(default='city', verbose_name=('Город'))
    category = models.ForeignKey(to=ApartCategory, on_delete=models.PROTECT, null=True, verbose_name=('Категория'))
    typeOfApart = models.ForeignKey(to=TypeOfApart, on_delete=models.PROTECT, null=True, verbose_name=('Тип недвижимости'))
    mebel = models.ForeignKey(to=Mebel, on_delete=models.PROTECT, null=True, verbose_name=('Мебель'))
    vidovaya = models.ForeignKey(to=Vidovaya, on_delete=models.PROTECT, null=True, verbose_name=('Видовая характеристика'))
    LcdOrS = models.ForeignKey(to=LcdOrSingle, on_delete=models.PROTECT, null=True, verbose_name=('ЖК или одиночное здание'))
    apartPlan = models.ForeignKey(to=ApartPlan, on_delete=models.PROTECT, null=True, verbose_name=('Планировка недвижимости'))
    DateOfBuild = models.DateField(verbose_name=('Дата постройки'))
    quantityRoom = models.CharField(max_length=10, default='1', verbose_name=('Количество комнат'))
    buildingAge = models.PositiveIntegerField(default=1, verbose_name=('Возраст здания'))
    developer = models.CharField(max_length=256, verbose_name=('Застройщик'))
    quantityOfMetres = models.PositiveIntegerField(default=1, verbose_name=('Количество квадратных метров'))
    livingSpace = models.PositiveIntegerField(default=1, verbose_name=('Жилая площадь'))
    infostracture = models.CharField(max_length=128, unique=True, verbose_name=('Инфраструктура'))
    qauntityOfFloors = models.PositiveIntegerField(default=1, verbose_name=('Количество этажей'))
    floorNumber = models.PositiveIntegerField(default=1, verbose_name=('Номер этажа'))
    apartmentNumber = models.PositiveIntegerField(default=1, verbose_name=('Номер квартиры'))
    quantityOfBathroom = models.PositiveIntegerField(default=1, verbose_name=('Количество ванных комнат'))
    dealType = models.TextField(default='Satilk', verbose_name=('Тип сделки'))
    location = models.TextField(default='Mersin/', verbose_name=('Местоположение'))

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'

    def __str__(self):
        return f'Недвижимость: {self.name} | Категория: {self.category.name}'

