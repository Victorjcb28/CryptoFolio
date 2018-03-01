from django.db import models

# Create your models here.

class Moneda(models.Model):
	symbol=models.CharField(max_length=100,primary_key=True,default="")
	name= models.CharField(max_length=50)
	cantidad= models.IntegerField()
	preciousd=models.FloatField()
	preciobtc=models.FloatField()



