from django.db import models

class Customer(models.Model):

    customer_name = models.CharField(max_length=200, null=True)
    joined_date = models.DateField(null=True)
    
    def __str__(self):

        return self.customer_name
    
class Product(models.Model):

    product_name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=0)

    def __str__(self):

        return self.product_name


class Bill(models.Model):

    customer = models.ForeignKey(Customer, related_name='customer_bill', on_delete=models.CASCADE)
    bill_number = models.CharField(max_length=10, null=True)
    bill_date = models.DateField(null=True)
    total_amount = models.FloatField(default=0)
    gst = models.FloatField(default=0)
    bill_amount = models.FloatField(default=0)

    def __str__(self):

        return self.customer.customer_name
    
class BillMaterials(models.Model):

    bill = models.ForeignKey(Bill, related_name='bill_products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    count = models.IntegerField(default=0)
    subtotal = models.FloatField(default=0)

    def __str__(self):
        return self.bill.bill_number


    
