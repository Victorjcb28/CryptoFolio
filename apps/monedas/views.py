from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from .forms import MonedaForm
from .models import Moneda
import requests



class index1(TemplateView):
	model=Moneda
	form_class=MonedaForm
	template_name='moneda/moneda_form.html'

def index(request):
	data = {}
    
	data["crypto_data"] = get_crypto_data()
    
	return render(request, "moneda/moneda_form.html",data)

def prueba(request):
	
	data = {}
    
	data["crypto_data"] = get_crypto_data()
	
	return render(request, 'moneda/prueba.html',data) 

# return the data received from api as json object
def get_crypto_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=100"
    #api_url="https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=USD"
    try:
        data = requests.get(api_url).json()
       
    except Exception as e:
        print(e)
        data = dict()

    return data


def get_crypto_data1():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=100"
    #api_url="http://api.bitcoinvenezuela.com/?html=no&currency=BTC&amount=1&to=USD"
    try:
        data1 = requests.get(api_url).json()
        
    except Exception as e:
        print(e)
        data1 = dict()

    return data1


