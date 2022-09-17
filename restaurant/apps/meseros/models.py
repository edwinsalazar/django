from ast import Delete
from django.db import models

# Create your models here.


class Meseros(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.IntegerField(verbose_name='dni')
    nombre = models.CharField(max_length=55, verbose_name='nombre')
    apellido = models.CharField(max_length=55, verbose_name='apellido')
    nacionalidad = models.CharField(max_length=255, verbose_name='nacionalidad')
    foto = models.ImageField(max_length=100, verbose_name='foto', upload_to='images/',default="")

    def delete(self, using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()
