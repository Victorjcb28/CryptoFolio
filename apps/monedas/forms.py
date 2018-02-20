from django import forms
from django.core.exceptions import ValidationError
from .models import Moneda



class MonedaForm(forms.ModelForm):

	class Meta:
		model= Moneda
		fields=[
			'name',
			'cantidad',
			'preciousd',
			'preciobtc',
			
					

		]

		labels={
			'name':'Nombre de la Moneda',
			'cantidad':'Cantidad',
			'preciousd':'Precio en $',
			'preciobtc':'Precio en BTC',
					
			
			
		}
		
		widgets={

			'name':forms.TextInput(attrs={'class':'form-control'}),
			'cantidad':forms.TextInput(attrs={'class':'form-control'}),
			'preciousd':forms.TextInput(attrs={'class':'form-control'}),
			'preciobtc':forms.TextInput(attrs={'class':'form-control'}),
			
			
			
		
		}

