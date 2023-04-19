from django import forms
from .models import User_mode
from .models import Seller_Model
from .models import Product
from .models import Cart_model

class Userform(forms.ModelForm):
    class Meta:
        model = User_mode
        fields = ['quantity','user_mob_no']

class Sellerform(forms.ModelForm):
    class Meta:
        model = Seller_Model
        fields = '__all__'

class Productform(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class Cartform(forms.ModelForm):

    class Meta:
        model = Cart_model
        fields = '__all__'

