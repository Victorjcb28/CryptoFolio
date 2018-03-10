from django.urls import path
from django.conf.urls import url
from . import views
from .views import tabmonedas,index,index1,get_crypto_data,moneda,MonedaCreate,MonedaInfo,MonedaInfo1,MonedaList

app_name = 'monedas'

urlpatterns = [
   url(r'^index/$', index, name="index"),
   url(r'^index/tabmonedas/$',tabmonedas, name='tabmonedas'),
   #url(r'^moneda/$',moneda, name='moneda'),
   #path('monedainfo/<str:pk>/', views.MonedaInfo.as_view(),name='moneda_info'),
   path('monedainfo/<str:pk>/', views.MonedaInfo1,name='moneda_info'),
   
   url(r'^monedaform/$',MonedaCreate, name='moneda_create'),
   url(r'^monedalist/$',MonedaList.as_view(), name='moneda_listar'),
   
   
   url(r'^index1/$', index1.as_view(),name='index1'),
   url(r'^index2/$', get_crypto_data,name='get'),

]