from rest_framework import serializers
from .models import Platos


class PlatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platos
        fields = ('__all__')
