from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('smoke/',views.smoke, name='smoke'),
    path('SME/',views.SME, name='SME'),
    path('Reflection/',views.Reflection, name='Reflection'),
    path('Reflectioneffect/',views.Reflectioneffect, name='Reflectioneffect'),
    path('Background/',views.Background, name='Background'),
    path('Backgroundeffect/',views.Backgroundeffect, name='Backgroundeffect'),
    path('Fire/',views.Fire,name='Fire'),
    path('FireBEffect/',views.FireBEffect,name='FireBEffect')

]