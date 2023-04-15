
from django.db import models

# Create your models here.
class Buyer_Model(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=30)
    user_mob_no = models.BigIntegerField()
    user_email = models.EmailField()
    user_address = models.CharField(max_length=60)

class Seller_Model(models.Model):

    Seller_id = models.CharField(max_length=30)
    company_business_name = models.CharField(max_length=30)
    Seller_name = models.CharField(max_length=30)
    Seller_mob_no = models.BigIntegerField()
    Seller_email = models.EmailField()
    Seller_address = models.CharField(max_length=60)

class Product_Model(models.Model):
    prd_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    Product_brand = models.CharField(max_length=30)
    Product_category = models.CharField(max_length=30)
    product_cost = models.CharField(max_length=30)
    product_image = models.ImageField(upload_to='static/media')
    product_releasedate = models.DateField()
    product_description = models.CharField(max_length=60)











