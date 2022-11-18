from django.db import models

# Create your models here.
class Data(models.Model):
    key = models.CharField(max_length=10,primary_key=True)
    value= models.CharField(max_length=100)

class  customer(models.Model):
    customer_code = models.CharField(max_length=10,primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    customer_address = models.CharField(max_length=100)
    order_code = models.CharField(max_length=10)
    order_sum_quantity = models.FloatField(null=True)
    order_total_price = models.FloatField(null=True)
    class Meta:
        db_table = "customer_code"
        managed = False
    def str(self):
        return self.customer_code

class  delivery(models.Model):
    delivery_type = models.CharField(max_length=50,primary_key=True)
    description = models.CharField(max_length=50)
    order_code = models.CharField(max_length=10)
    order_sum_quantity = models.FloatField(null=True)
    order_total_price = models.FloatField(null=True)
    class Meta:
        db_table = "delivery_type"
        managed = False
    def str(self):
        return self.delivery_type

class  discount(models.Model):
    product_code = models.CharField(max_length=10,primary_key=True)
    quantity = models.FloatField(null=True)
    class Meta:
        db_table = "delivery_type"
        managed = False
    def str(self):
        return self.delivery_type

class  order(models.Model):
    order_code = models.CharField(max_length=10,primary_key=True)
    sum_quantity = models.FloatField(null=True)
    total_price = models.FloatField(null=True)
    customer_code = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=20)
    delivery_type = models.CharField(max_length=50)
    class Meta:
        db_table = "delivery_type"
        managed = False
    def str(self):
        return self.delivery_type


class payment(models.Model):
    payment_method = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=20, null=True)
    order_code = models.CharField(max_length=10, null=True)
    order_sum_quantity = models.FloatField(null=True, blank=True)
    order_total_price = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = "payment"
        managed = False
    def __str__(self):
        return "%s %s" % (self.payment_method)    

class product(models.Model):
    product_code = models.CharField(max_length=10, primary_key=True)
    product_name = models.CharField(max_length=50, primary_key=True)
    product_type = models.CharField(max_length=20, primary_key=True)
    product_brand = models.CharField(max_length=20, primary_key=True)
    price = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = "product"
        unique_together = (("product_code", "product_name"),)
        managed = False
    def __str__(self):
        return "%s %s" % (self.product_code)    

class product_warehouse(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    product_name = models.CharField(max_length=50, primary_key=True)
    quantity =models.FloatField(null=True, blank=True) 
    unit = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = "product_warehouse"
        unique_together = (("code", "product_name"),)
        managed = False
    def __str__(self):
        return "%s %s" % (self.code)  

class promotion(models.Model):
    product_code = models.CharField(max_length=10, primary_key=True)
    product_name = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=100, null=True)
    class Meta:
        db_table = "promotion"
        unique_together = (("product_code", "product_name"),)
        managed = False
    def __str__(self):
        return "%s %s" % (self.product_code)  
