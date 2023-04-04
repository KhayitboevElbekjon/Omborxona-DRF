from .models import *
from rest_framework import serializers
class OmborSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ombor
        fields='__all__'

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mahsulot
        fields='__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields='__all__'