from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomerView(APIView):

    def get(self, request, id = None):

        if id == None:

            all_customers = Customer.objects.all()

            all_customer_data = []

            for customer in all_customers:

                customer_dataset = {
                    "customer_name": customer.customer_name,
                    "address": customer.address,
                    "phone_number": customer.phone_number,
                    "age": customer.age,
                    "company_name": customer.company_name,
                    "member_since": customer.member_since
                }

                all_customer_data.append(customer_dataset)

            return Response(all_customer_data)
        
        else:

            selected_customer = Customer.objects.get(id = id)

            customer_dataset = {
                "customer_name": selected_customer.customer_name,
                "address": selected_customer.address,
                "phone_number": selected_customer.phone_number,
                "age": selected_customer.age,
                "company_name": selected_customer.company_name,
                "member_since": selected_customer.member_since
            }

            return Response(customer_dataset)
        
    def post(self, request):

        d = request.data

        new_customer_data = Customer(customer_name = d['customer_name'], address = d['address'], phone_number = d['phone_number'], age = d['age'], company_name = d['company_name'], member_since = d['member_since'])

        new_customer_data.save()

        return Response("New customer data added")
    
    def patch(self, request, id):

        d = request.data

        selected_customer = Customer.objects.filter(id = id)

        selected_customer.update(customer_name = d['customer_name'], address = d['address'], phone_number = d['phone_number'], age = d['age'], company_name = d['company_name'], member_since = d['member_since'])

        return Response("Customer data updated")
    
    def delete(self, request, id):

        selected_customer = Customer.objects.get(id = id)

        selected_customer.delete()

        return Response("Customer data deleted")


class ProductView(APIView):

    def get(self, request, id = None):

        if id == None:

            all_products = Product.objects.all()

            all_product_data = Product_Serializer(all_products, many=True).data

            return Response(all_product_data)
        
        else:

            selected_product = Product.objects.get(id = id)

            product_data = Product_Serializer(selected_product).data

            return Response(product_data)
        
    def post(self, request):

        new_product_data = Product_Serializer(data=request.data)

        if new_product_data.is_valid():

            new_product_data.save()

            return Response("Product data added")
        
        else:

            return Response(new_product_data.errors)
    
    def patch(self, request, id):

        selected_product = Product.objects.get(id = id)

        product_data = Product_Serializer(selected_product, data=request.data, partial=True)

        if product_data.is_valid():

            product_data.save()

            return Response("Product data updated")
        
        else:

            return Response(product_data.errors)
        
    def delete(self, request, id):

        selected_product = Product.objects.get(id = id)

        selected_product.delete()

        return Response("Product data updated")


class OrderDetailsView(APIView):

    def get(self, request, id = None):

        if id == None:

            all_orders = OrdersDetails.objects.all()

            order_serializer = OrderDetails_Serializers(all_orders, many=True)

            return Response(order_serializer.data)
        
        else:

            order = OrdersDetails.objects.get(id = id)

            order_serializer = OrderDetails_Serializers(order)

            return Response(order_serializer.data)

    def post(self, request):

        details_data = request.data[0]

        product_data = request.data[1]

        order_details = OrdersDetails(customer_id = details_data['customer_id'], bill_date = details_data['bill_date'])

        order_details.save()

        product_sum = 0

        for a in product_data:

            product = Product.objects.get(id = a['product_id'])

            product_amount = a['quantity'] * product.price

            product_gst_amount = (product_amount * product.gst) / 100

            product_sub_total = product_amount + product_gst_amount

            product_sum = product_sum + product_sub_total

            ordered_products = OrderedProducts(order_details_id = order_details.id, product_id = a['product_id'], quantity = a['quantity'], amount = product_amount, gst_amount = product_gst_amount, sub_total = product_sub_total)

            ordered_products.save()

        order_details_filter = OrdersDetails.objects.filter(id = order_details.id)

        order_details_filter.update(bill_amount = product_sum)

        return Response("Order Placed")
    
    def patch(self, request, id):

        details_data = request.data[0]

        product_data = request.data[1]

        order_filter = OrdersDetails.objects.filter(id = id)

        order_filter.update(bill_date = details_data['bill_date'])

        for a in product_data:

            if a['new'] == True:

                product = Product.objects.get(id = a['product_id'])

                product_amount = a['quantity'] * product.price

                product_gst_amount = (product_amount * product.gst) / 100

                product_sub_total = product_amount + product_gst_amount

                product_sum = product_sum + product_sub_total

                ordered_products = OrderedProducts(order_details_id = id, product_id = a['product_id'], quantity = a['quantity'], amount = product_amount, gst_amount = product_gst_amount, sub_total = product_sub_total)

                ordered_products.save()

            elif a['delete'] == True:

                product = OrderedProducts.objects.get(id = a['id'])

                product.delete()

            elif a['update'] == True:

                ordered_product_filter = OrderedProducts.objects.filter(id = a['id'])

                product = Product.objects.get(id = a['product_id'])

                product_amount = a['quantity'] * product.price

                product_gst_amount = (product_amount * product.gst) / 100

                product_sub_total = product_amount + product_gst_amount

                product_sum = product_sum + product_sub_total

                ordered_product_filter.update(product_id = a['product_id'], quantity = a['quantity'], amount = product_amount, gst_amount = product_gst_amount, sub_total = product_sub_total)

        products_to_order = OrderedProducts.objects.filter(order_details_id = id)

        final_subtotal = 0

        for z in products_to_order:

            final_subtotal = final_subtotal + z.sub_total

        return Response("Order data updated")
    
    def delete(self, request, id):

        order = OrdersDetails.objects.get(id = id)

        order.delete()

        return Response("Order data deleted")


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)

        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):

    serializer_class = MyTokenObtainPairSerializer


class TestView(APIView):

    def get(self, request, id = None):

        if id == None:

            return Response(TestSerializer(Test.objects.all(), many=True).data)
        
        else:

            return Response(TestSerializer(Test.objects.get(id = id)).data)

    def post(self, request):

        data = request.data

        new = Test(customer_name = data['name'], username = data['username'], age = data['age'])

        new.save()

        return Response("Data Saved")
    
    def patch(self, request, id):

        data = request.data

        Test.objects.filter(id = id).update(customer_name = data['name'], username = data['username'], age = data['age'])

        return Response("Data Updated")
    
    def delete(self, request, id):

        Test.objects.get(id = id).delete()

        return Response("Data Deleted")


class Sample(APIView):

    def get(self, request):

        dataset = {
            "Django": True
        }

        return Response(dataset)

    def post(self,request):

        pass

    def patch(self,request):

        pass

    def put(self,request):

        pass

    def delete(self,request):

        pass
    
    
    

