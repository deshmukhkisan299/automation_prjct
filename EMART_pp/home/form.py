from django import forms
from .models import Usermode
from .models import Seller_Model
from .models import Product1


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
        model = Product1
        fields = '__all__'



