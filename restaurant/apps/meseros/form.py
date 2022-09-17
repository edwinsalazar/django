from django import forms
from .models import Meseros


class MeserosForm(forms.ModelForm):
    class Meta:
        model = Meseros
        fields = '__all__'
