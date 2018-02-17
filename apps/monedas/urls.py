from django.urls import path
from django.conf.urls import url
from .views import prueba,index,index1,get_crypto_data

app_name = 'monedas'

urlpatterns = [
   url(r'^index/$', index, name="index"),
   url(r'^index/prueba/$',prueba, name='prueba'),
   url(r'^index1/$', index1.as_view(),name='index1'),
   url(r'^index2/$', get_crypto_data,name='get'),

]