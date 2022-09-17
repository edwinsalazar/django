from django.contrib import admin
from .models import Meseros

@admin.register(Meseros)
class MeserosAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellido', 'nacionalidad', )
