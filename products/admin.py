from django.contrib import admin
from .models import ApartCategory, TypeOfApart, Mebel, Vidovaya, LcdOrSingle, ApartPlan, Apart
from django.contrib.auth.models import Group, User

admin.site.site_header = 'Nolabel'
admin.site.site_title = 'Админ панель'
admin.site.index_title = 'Главная'

Group._meta.verbose_name_plural = 'Группы'
User._meta.verbose_name_plural = 'Пользователи'

admin.site.register(ApartCategory)
admin.site.register(Apart)
admin.site.register(TypeOfApart)
admin.site.register(Mebel)
admin.site.register(Vidovaya)
admin.site.register(LcdOrSingle)
admin.site.register(ApartPlan)
