from django.db import models

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.IntegerField(verbose_name='dni')
    nombre = models.CharField(max_length=55, verbose_name='nombre')
    apellido = models.CharField(max_length=55, verbose_name='apellido')
    nacionalidad = models.CharField(max_length=50, verbose_name='nacionalidad')