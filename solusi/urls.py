"""solusi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from solusiweb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    #path('studentlib/', admin.site.urls),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),

    path('vice/', views.vice, name='vice'),
    path('provice/', views.provice, name='provice'),
    path('daf/', views.daf, name='daf'),
    path('studentaff/', views.studentaff, name='studentaff'),
    path('register/', views.register, name='register'),

    path('agric/', views.agric, name='agric'),
    path('commerce/', views.commerce, name='commerce'),
    path('education/', views.education, name='education'),
    path('health/', views.health, name='health'),
    path('theology/', views.theology, name='theology'),
    path('graduation/', views.graduation, name='graduation'),

    path('about/', views.about, name='about'),
    path('alumini/', views.alumini, name='alumini'),
    path('contact/', views.contact, name='contact'),
    path('library/', views.library, name='library'),
    path('studentlib/', views.studentlib, name='studentlib'),

    path('agribusiness/', views.agribusiness, name='agribusiness'),
    path('clothing/', views.clothing, name='clothing'),
    path('science/', views.science, name='science'),
    path('matnum/', views.matnum, name='matnum'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('admin/', views.admin, name='admin'),#admins list
    path('nursing/', views.nursing, name='nursing'),

    path('inAccounts/', views.inAccounts, name='inAccounts'),
    path('infosys/', views.infosys, name='infosys'),
    path('infinance/', views.infinance, name='infinance'),
    path('inmarketing/', views.inmarketing, name='inmarketing'),
    path('inmanagement/', views.inmanagement, name='inmanagement'),


    path('contact/', views.contact, name='contact'),
    path('thanks/', views.thanks, name='thanks'),

    path('educat/', views.educat, name='educat'),
    path('healt/', views.healt, name='healt'),
    path('theol/', views.theol, name='theol'),


    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

