
from django.db import models

# Create your models here.
class Usermode(models.Model):
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

class Product1(models.Model):
    product_name = models.CharField(max_length=30)
    Product_brand = models.CharField(max_length=30)
    Product_category = models.CharField(max_length=30)
    product_cost = models.IntegerField()
    prod_quantity = models.IntegerField(default=1)
    product_image = models.ImageField(upload_to='static/media/')
    product_releasedate = models.DateField()
    product_description = models.CharField(max_length=60)


class Customer1(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)


    def register(self):
        self.save()



    def isExists(self):
        if Customer1.objects.filter(phone=self.phone):
            return True
        else:
            False




class Cart1(models.Model):
    phone=models.CharField(max_length=10)
    Product_brand=models.ForeignKey(Product1,on_delete=models.CASCADE)
    product_image=models.ImageField(null=True,blank=True)
    quantity=models.PositiveIntegerField(default=1)
    product_cost=models.IntegerField(default=0)



STATUS_CHOICE = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)






class order_details(models.Model):
    user=models.IntegerField(default=True)
    Product_name= models.CharField(max_length=250)
    image=models.ImageField(null=True,blank=True)
    Qty=models.PositiveIntegerField(default=1)
    price=models.IntegerField()
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,default='pendding',choices=STATUS_CHOICE)




