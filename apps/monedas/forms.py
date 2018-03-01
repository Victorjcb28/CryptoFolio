from django import forms
from django.core.exceptions import ValidationError
from .models import Moneda



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
			'symbol':forms.TextInput(attrs={'class':'symbol form-control','disabled':'true','size':'5%'},),
			'name':forms.TextInput(attrs={'class':'name form-control','disabled':'true','size':'5%'},),
			'cantidad':forms.TextInput(attrs={'class':'cantidad form-control','size':'5%'},),
			'preciousd':forms.TextInput(attrs={'class':'preciousd form-control','disabled':'true','size':'5%'},),
			'preciobtc':forms.TextInput(attrs={'class':'preciobtc form-control','disabled':'true','size':'5%'},),
			
			
			
		
		}

