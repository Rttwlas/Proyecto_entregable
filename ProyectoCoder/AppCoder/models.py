from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateTimeField()
    edad = models.IntegerField()
    
