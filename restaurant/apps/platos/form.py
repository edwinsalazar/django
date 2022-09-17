from django import forms
from .models import Platos


class PlatosForm(forms.ModelForm):
    class Meta:
        model = Platos
        fields = '__all__'
