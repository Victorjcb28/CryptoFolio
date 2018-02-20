from django.db import models

# Create your models here.

class Moneda(models.Model):

	name= models.CharField(max_length=50)
	cantidad= models.IntegerField()
	preciousd=models.FloatField()
	preciobtc=models.FloatField()



