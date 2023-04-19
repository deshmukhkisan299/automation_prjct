
from django.db import models

# Create your models here.
class User_mode(models.Model):
    quantity=models.IntegerField()
    user_name = models.CharField(max_length=30)
    user_mob_no = models.BigIntegerField()
    alternate_No= models.BigIntegerField()
    user_email = models.EmailField()
    user_address = models.CharField(max_length=60)

class Seller_Model(models.Model):

    Seller_id = models.CharField(max_length=30)
    company_business_name = models.CharField(max_length=30)
    Seller_name = models.CharField(max_length=30)
    Seller_mob_no = models.BigIntegerField()
    Seller_email = models.EmailField()
    Seller_address = models.CharField(max_length=60)

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    Product_brand = models.CharField(max_length=30)
    Product_category = models.CharField(max_length=30)
    product_cost = models.CharField(max_length=30)
    product_image = models.ImageField(upload_to='static/media')
    product_releasedate = models.DateField()
    product_description = models.CharField(max_length=60)




class Cart_model(models.Model):
    Username=models.CharField(max_length=20)
    Product_brand=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_image=models.ImageField(null=True,blank=True)
    quantity=models.PositiveIntegerField(default=1)
    product_cost=models.IntegerField(default=0)





