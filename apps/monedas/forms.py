from django import forms
from django.core.exceptions import ValidationError
from .models import Moneda



class MonedaForm(forms.ModelForm):

	class Meta:
		model= Moneda
		fields=[
			'nombre',
			'cantidad',
			
					

		]

		labels={
			'nombre':'Nombre de la Moneda',
			'cantidad':'Cantidad',
					
			
			
		}
		
		widgets={

			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'cantidad':forms.TextInput(attrs={'class':'form-control'}),
			
			
			
		
		}

