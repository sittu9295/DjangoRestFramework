from rest_framework import serializers
from .models import *

class Customer_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Customer
        fields = '__all__' 


class Product_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = '__all__'
