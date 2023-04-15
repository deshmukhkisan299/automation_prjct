from django import forms
from .models import Buyer_Model
from .models import Seller_Model
from .models import Product_Model
class Userform(forms.ModelForm):

    class Meta:
        model = Buyer_Model
        fields = '__all__'

class Sellerform(forms.ModelForm):

    class Meta:
        model = Seller_Model
        fields = '__all__'

class Productform(forms.ModelForm):

    class Meta:
        model = Product_Model
        fields = '__all__'



