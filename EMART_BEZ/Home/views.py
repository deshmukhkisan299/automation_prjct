from django.shortcuts import render,HttpResponseRedirect
from .form import Userform
from .form import Sellerform
from .form import Productform
from .models import Product_Model
from .models import Buyer_Model
from .models import Seller_Model
from django.contrib.auth.decorators import login_required
# Create your views here.

def product_show(r):
    form = Product_Model.objects.all()
    return render(r,'home/product_show.html',{'form':form})


@login_required()
def User_view(r):
    form=Userform()
    if r.method=="POST":
        form=Userform(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
    return render(r,'home/userform.html',{'form':form})

def Seller_view(r):
    form=Sellerform()
    if r.method=="POST":
        form=Sellerform(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
    return render(r,'home/Sellerform.html',{'form':form})



def Product_view(r):
    form=Productform()
    if r.method=="POST":
        form=Productform(r.POST,r.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productshow')
    return render(r,'home/Productform.html',{'form':form})



