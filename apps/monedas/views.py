from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from .forms import MonedaForm,HistMonedaForm
from .models import Moneda,HistMoneda
import requests
import datetime



class index1(TemplateView):
	model=Moneda
	form_class=MonedaForm
	template_name='moneda/moneda_form.html'

def index(request):
	data = {}
    
	data["crypto_data"] = get_crypto_data()
    
	return render(request, "moneda/index.html",data)

def tabmonedas(request):
	
	data = {}
    
	data["crypto_data"] = get_crypto_data()
	
	return render(request, 'moneda/tabmonedas.html',data) 

def moneda(request):
	
	data = {}
    
	data["crypto_data"] = get_crypto_data()
	
	return render(request, 'moneda/moneda_form.html',data) 

class MonedaInfo1(TemplateView):
	model=Moneda
	form_class=MonedaForm
	template_name='moneda/moneda_info.html'

#malo
def MonedaInfo1(request , pk):
	moneda=Moneda.objects.get(symbol=pk)
	moneda1=HistMoneda.objects.filter(symbol=pk)

	if request.method=='GET':
		form=MonedaForm(instance=moneda)
	else:
		form=MonedaForm(request.POST,instance=moneda)
		if form.is_valid():
			form_data=form.cleaned_data
			symbol=form_data.get('symbol')
			date=datetime.date.today()
			name=form_data.get('name')
			usd=form_data.get('preciousd')
			btc=form_data.get('preciobtc')
			cantidad=form_data.get('cantidad')

			obj=Moneda.objects.filter(symbol=pk).update(cantidad=cantidad)
			obj1=HistMoneda.objects.create(symbol=symbol,name=name,cantidad=cantidad,preciousd=usd,preciobtc=btc,date=date)
			

		return redirect('moneda:moneda_create')
	return render(request,'moneda/moneda_info.html',{'form':form,"monedas":moneda1})

class MonedaInfo(UpdateView):
	model = Moneda
	second_model=HistMoneda	
	form_class = MonedaForm
	second_form_class=HistMonedaForm
	moneda=HistMoneda.objects.all()

	
	success_url= reverse_lazy('moneda:index')	
	template_name= 'moneda/moneda_info.html'

	

class MonedaList(ListView):
	model= HistMoneda
	template_name= 'moneda/tabmonedahist.html'

def MonedaCreate(request):
	moneda=Moneda.objects.all()
	form= MonedaForm(request.POST or None,request.FILES or None)

	context={

		"form":form,
		"monedas":moneda,
			}
	context["crypto_data"] = get_crypto_data()
	if form.is_valid():
		instance=form.save(commit=False)
		#form.save()
		form_data=form.cleaned_data
		symbol=form_data.get('symbol')
		date=datetime.date.today()
		name=form_data.get('name')
		usd=form_data.get('preciousd')
		btc=form_data.get('preciobtc')
		cantidad=form_data.get('cantidad')

		obj=Moneda.objects.create(symbol=symbol,name=name,cantidad=cantidad,preciousd=usd,preciobtc=btc)
		obj1=HistMoneda.objects.create(symbol=symbol,name=name,cantidad=cantidad,preciousd=usd,preciobtc=btc,date=date)
		

	return render(request,'moneda/moneda_form.html',context)	
	

	
# return the data received from api as json object
def get_crypto_data():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
    #api_url="https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=USD"
    try:
        data = requests.get(api_url).json()
       
    except Exception as e:
        print(e)
        data = dict()

    return data


def get_crypto_data1():
    api_url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
    #api_url="http://api.bitcoinvenezuela.com/?html=no&currency=BTC&amount=1&to=USD"
    try:
        data1 = requests.get(api_url).json()
        
    except Exception as e:
        print(e)
        data1 = dict()

    return data1


