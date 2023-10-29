"""
URL configuration for TurkishProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from products.views import index, search, about_us, tovar, search_by_category, search_by_type, search_by_year, contact_us, buying_in_Kipr,buying_in_Turk, health, how_are_we, why_turk, rasxodi, Turkish_citezenship, VidNaShitelstvo, procedure, tapu, fondi, trusting



urlpatterns = [
    path('djsanhjfab8743gbhvbfdvbkhjdsbhgfb43bfgdnjgfdn/', admin.site.urls),
    path('', index, name='index'),
    path('search/category/<int:category_id>/', search_by_category, name='category'),
    path('search/type/<int:type_id>/', search_by_type, name='type'),
    path('search/year/', search_by_year, name='search_by_year'),
    path('search/', search, name='search'),
    path('about_us/', about_us, name='about_us'),
    path('tovar/', tovar, name='tovar'),
    path('contact_us/', contact_us, name='contact_us'),
    path('buying_in_Kipr/', buying_in_Kipr, name='buying_in_Kipr'),
    path('buying_in_Turk/', buying_in_Turk, name='buying_in_Turk'),
    path('health/', health, name='health'),
    path('how_are_we/', how_are_we, name='how_are_we'),
    path('rasxodi/', rasxodi, name='rasxodi'),
    path('Turkish_citezenship/', Turkish_citezenship, name='Turkish_citezenship'),
    path('VidNaShitelstvo/', VidNaShitelstvo, name='VidNaShitelstvo'),
    path('procedure/', procedure, name='procedure'),
    path('tapu/', tapu, name='tapu'),
    path('fondi/', fondi, name='fondi'),
    path('trusting/', trusting, name='trusting'),
    path('why_turk/', why_turk, name='why_turk'),

]




if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)