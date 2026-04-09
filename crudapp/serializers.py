from rest_framework import serializers
from .models import Item

def des_lessthan_30(description):
    if len(description)>30:
        raise serializers.ValidationError("Description is TO large")

class ItemSerializer(serializers.ModelSerializer):
    description = serializers.CharField(validators=[des_lessthan_30]) 

    class Meta:
        model = Item
        fields = '__all__'