from django.db import models

# Create your models here.

class ApartCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.name

class TypeOfApart(models.Model):
    type = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.type

class Mebel(models.Model):
    type = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.type
class Vidovaya(models.Model):
    type = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.type

class LcdOrSingle(models.Model):
    type = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.type

class ApartPlan(models.Model):
    type = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return self.type


class Apart(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='products_images')
    city = models.TextField(default='city')
    category = models.ForeignKey(to=ApartCategory, on_delete=models.PROTECT, null=True)
    typeOfApart = models.ForeignKey(to=TypeOfApart, on_delete=models.PROTECT, null=True)
    mebel = models.ForeignKey(to=Mebel, on_delete=models.PROTECT, null=True)
    vidovaya = models.ForeignKey(to=Vidovaya, on_delete=models.PROTECT, null=True)
    LcdOrS = models.ForeignKey(to=LcdOrSingle, on_delete=models.PROTECT, null=True)
    apartPlan = models.ForeignKey(to=ApartPlan, on_delete=models.PROTECT, null=True)
    DateOfBuild = models.DateField()
    quantityRoom = models.CharField(max_length=10, default='1')
    buildingAge = models.PositiveIntegerField(default=1)
    developer = models.CharField(max_length=256)
    quantityOfMetres = models.PositiveIntegerField(default=1)
    infostracture = models.CharField(max_length=128, unique=True)
    qauntityOfFloors = models.PositiveIntegerField(default=1)
    apartmentNumber = models.PositiveIntegerField(default=1)
    quantityOfBathroom = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Недвижимость: {self.name} | Категория: {self.category.name}'


