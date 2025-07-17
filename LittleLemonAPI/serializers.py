from rest_framework import serializers
from restaurant.models import Menu

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','title','price','inventory']