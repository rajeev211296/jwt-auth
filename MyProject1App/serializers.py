from rest_framework import serializers
from .models import *
class ModelSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'
