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


class OrderedProducts_Serializer(serializers.ModelSerializer):

    class Meta:

        model = OrderedProducts
        fields = '__all__'


class OrderDetails_Serializers(serializers.ModelSerializer):

    customer = Customer_Serializer()
    bill_products = OrderedProducts_Serializer(many=True)

    class Meta:

        model = OrdersDetails
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):

    class Meta:

        model = Test
        fields = '__all__'