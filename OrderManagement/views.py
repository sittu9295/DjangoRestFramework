from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class BasicApiView(APIView):

    def get(self, request):

        user_data = {
            "name": "Kishore",
            "age": 25
        }

        return Response(user_data)
    
    def post(self, request):

        print(request.data)

        return Response("Data Saved")
    

class CustomerView(APIView):

    def get(self, request, id=None):

        if id == None:

            customer_all = Customer.objects.all()

            customer_data = Customer_Serializer(customer_all, many=True).data

            return Response({'response': 'success', 'data': customer_data})
        
        else:

            customer_get = Customer.objects.get(id=id)

            customer_data = Customer_Serializer(customer_get).data

            return Response({'response': 'success', 'data': customer_data})
    
    def post(self, request):

        customer_data = Customer_Serializer(data=request.data)

        if customer_data.is_valid():

            customer_data.save()

            return Response({'response': 'success', 'message': 'Data Saved'})

        else:

            return Response({'response': 'error', 'message': customer_data.errors})
    
    def patch(self, request, id):

        customer_get = Customer.objects.get(id=id)

        customer_data = Customer_Serializer(customer_get, data=request.data, partial=True)

        if customer_data.is_valid():

            customer_data.save()

            return Response({'response': 'success', 'message': 'Data Updated'})
        
        else:
            
            return Response({'response': 'error', 'message': customer_data.errors})

    
    def delete(self, request, id):

        customer = Customer.objects.get(id=id)

        customer.delete()

        return Response({'response': 'success', 'message': 'Data Deleted'})
    

class ProductView(APIView):

    def get(self, request, id=None):

        if id == None:

            product_all = Product.objects.all()

            product_data = Product_Serializer(product_all, many=True).data

            return Response({'response': 'success', 'data': product_data})
        
        else:

            product_get = Product.objects.get(id=id)

            product_data = Product_Serializer(product_get).data

            return Response({'response': 'success', 'data': product_data})
    
    def post(self, request):

        product_data = Product_Serializer(data=request.data)

        if product_data.is_valid():

            product_data.save()

        return Response({'response': 'success', 'message': 'Data Saved'})
    
    def patch(self, request, id):

        product_get = Product.objects.get(id=id)

        product_data = Product_Serializer(product_get, data=request.data, partial=True)

        if product_data.is_valid():

            product_data.save()

        return Response({'response': 'success', 'message': 'Data Updated'})
    
    def delete(self, request, id):

        product = Product.objects.get(id=id)

        product.delete()

        return Response({'response': 'success', 'message': 'Data Deleted'})


class BillView(APIView):

    def post(self, request):

        data = request.data

        bill_details = Bill(customer_id = data['customer_id'], bill_number = data['bill_number'], bill_date = data['bill_date'], gst = data['gst'])

        bill_details.save()

        return Response({'response': 'success', 'message': 'Data Saved'})

