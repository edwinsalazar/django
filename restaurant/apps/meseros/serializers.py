from rest_framework import serializers
from apps.meseros.models import Meseros

class MeserosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meseros
        fields = ('__all__')
