from django.contrib import admin
from .models import User_Model
from .models import Cart1
from .models import order_details
# Register your models here.


class AdminCustomer(admin.ModelAdmin):
    list_display=['id','username','phone']

class AdminCart(admin.ModelAdmin):
    list_display=['id','phone','Product_brand','product_image','quantity','product_cost']

class Adminorder(admin.ModelAdmin):
    list_display=['id','user','Product_name','image','Qty','price','ordered_date','status']

admin.site.register(User_Model,AdminCustomer)
admin.site.register(Cart1,AdminCart)
admin.site.register(order_details,Adminorder)
