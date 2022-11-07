from django.db import models
from datetime import datetime

# Create your models here.

class familiar1(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    nacimiento = models.DateField()
