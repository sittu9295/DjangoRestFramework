from django.db import models

class Customer(models.Model):

    customer_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=10, null=True)
    age = models.IntegerField(default=0)
    company_name = models.CharField(max_length=100, null=True)
    member_since = models.DateField(null=True)

    def __str__(self):
        
        return self.customer_name

class Product(models.Model):

    product_name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=0)
    gst = models.FloatField(default=0)


class OrdersDetails(models.Model):

    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    bill_date = models.DateField(null=True)
    bill_amount = models.FloatField(default=0)

class OrderedProducts(models.Model):

    order_details = models.ForeignKey(OrdersDetails, related_name="bill_products", null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    gst_amount = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)