from django.contrib import admin

# Register your models here.
from products.models import ApartCategory, Apart, TypeOfApart, Mebel, Vidovaya, LcdOrSingle, ApartPlan

admin.site.register(ApartCategory)
admin.site.register(Apart)
admin.site.register(TypeOfApart)
admin.site.register(Mebel)
admin.site.register(Vidovaya)
admin.site.register(LcdOrSingle)
admin.site.register(ApartPlan)