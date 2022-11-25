from rest_framework import serializers
from gui.models import ShoppingList


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = '__all__'