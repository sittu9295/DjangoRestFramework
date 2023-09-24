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

class Bill_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Bill
        fields = '__all__'

class BillMaterials_Serializer(serializers.ModelSerializer):

    class Meta:

        model = BillMaterials
        fields = '__all__'



class Bill_Get_Serializer(serializers.ModelSerializer):

    bill_products = BillMaterials_Serializer(many=True)

    class Meta:

        model = Bill
        fields = '__all__'


