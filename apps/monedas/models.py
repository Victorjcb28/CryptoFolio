from django.db import models

# Create your models here.

class Moneda(models.Model):

	nombre= models.CharField(max_length=50)
	cantidad= models.IntegerField()