from django.db import models
from django.conf import settings
from django.forms import CharField


# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=1000)
    hp = models.IntegerField(blank=True, null=True)        
    attack = models.IntegerField(blank=True, null=True)          
    defense = models.IntegerField(blank=True, null=True)         
    type = models.CharField(max_length = 1000)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,blank = True, null = True)


