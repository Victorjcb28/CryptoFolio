from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from django.urls import reverse_lazy
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
    
	return render(request, "moneda/index.html",data)

def tabmonedas(request):
	
	data = {}
    
	data["crypto_data"] = get_crypto_data()
	
	return render(request, 'moneda/tabmonedas.html',data) 

def moneda(request):
	
	data = {}
    
	data["crypto_data"] = get_crypto_data()
	
	return render(request, 'moneda/moneda_form.html',data) 


class MonedaCreate(CreateView):
	model= Moneda
	template_name="moneda/moneda_create.html"
	form_class=MonedaForm
	success_url=reverse_lazy('monedas:index')

	def get_context_data(self, **kwargs):
		context = super(MonedaCreate, self).get_context_data(**kwargs)
		pk = self.kwargs.get('pk', 0)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		pkk=kwargs['pk']
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.persona = form2.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))


	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.persona = form2.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))

	
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


