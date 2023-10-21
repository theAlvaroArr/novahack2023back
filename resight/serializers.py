from rest_framework import serializers
from .models import Gafa

class GafaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gafa
        fields = '__all__'