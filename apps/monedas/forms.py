from django import forms
from django.core.exceptions import ValidationError
from .models import Moneda,HistMoneda



class MonedaForm(forms.ModelForm):

	class Meta:
		model= Moneda
		fields=[
			
			'symbol',
			'name',
			'cantidad',
			'preciousd',
			'preciobtc',
			
					

		]

		labels={
			
			'symbol':'Simbologia',
			'name':'Nombre de la Moneda',
			'cantidad':'Cantidad',
			'preciousd':'Precio en $',
			'preciobtc':'Precio en BTC',
					
			
			
		}
		
		widgets={
			
			'symbol':forms.TextInput(attrs={'class':'symbolo form-control','size':'5%','readonly':'true',},),
			'name':forms.TextInput(attrs={'class':'name form-control','size':'5%','readonly':'true',},),
			'cantidad':forms.TextInput(attrs={'class':'cantidad form-control','size':'5%'},),
			'preciousd':forms.TextInput(attrs={'class':'preciousd form-control','size':'5%','readonly':'true',},),
			'preciobtc':forms.TextInput(attrs={'class':'preciobtc form-control','size':'5%','readonly':'true',},),
			
			
			
			
		
		}

class HistMonedaForm(forms.ModelForm):

	class Meta:
		model= HistMoneda
		fields=[
			'date',			
			'symbol',
			'name',
			'cantidad',
			'preciousd',
			'preciobtc',
			
					

		]

		labels={
			'date':'date',
			'symbol':'Simbologia',
			'name':'Nombre de la Moneda',
			'cantidad':'Cantidad',
			'preciousd':'Precio en $',
			'preciobtc':'Precio en BTC',
					
			
			
		}
		
		widgets={
			
			'symbol':forms.TextInput(attrs={'class':'symbolo form-control','size':'5%','readonly':'true',},),
			'name':forms.TextInput(attrs={'class':'name form-control','size':'5%','readonly':'true',},),
			'cantidad':forms.TextInput(attrs={'class':'cantidad form-control','size':'5%'},),
			'preciousd':forms.TextInput(attrs={'class':'preciousd form-control','size':'5%','readonly':'true',},),
			'preciobtc':forms.TextInput(attrs={'class':'preciobtc form-control','size':'5%','readonly':'true',},),
			'date':forms.TextInput(attrs={'class':' form-control','size':'5%','readonly':'true',},),
			
			
			
		
		}


