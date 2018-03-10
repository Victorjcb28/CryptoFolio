from django.db import models
import datetime

# Create your models here.

class Moneda(models.Model):
	
	symbol=models.CharField(max_length=100,primary_key=True,default="")
	name= models.CharField(max_length=50)
	cantidad= models.IntegerField(null=True)
	preciousd=models.FloatField(null=True)
	preciobtc=models.FloatField(null=True)




class HistMoneda(models.Model):

	symbol=models.CharField(max_length=100)
	name= models.CharField(max_length=50)
	cantidad= models.IntegerField(null=True)
	preciousd=models.FloatField(null=True)
	preciobtc=models.FloatField(null=True)
	date = models.DateField(default=datetime.date.today)

