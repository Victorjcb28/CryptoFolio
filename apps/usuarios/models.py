from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    MY_CHOICES = (
        ('opt0', 'ADMINISTRADOR'),
        ('opt1', 'USUARIO'),
    )
    tipo = models.CharField(max_length=50, choices=MY_CHOICES)
    image=models.FileField(blank=True,null=True,default="img")#no colocar barra primero
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()