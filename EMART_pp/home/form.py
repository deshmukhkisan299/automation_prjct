from django import forms
from .models import Usermode, Seller_Model, Product_details


class Userform(forms.ModelForm):
    class Meta:
        model = Usermode
        fields = ['user_mob_no']

class Sellerform(forms.ModelForm):
    class Meta:
        model = Seller_Model
        fields = '__all__'

class Productform(forms.ModelForm):

    class Meta:
        model = Product_details
        fields = '__all__'



