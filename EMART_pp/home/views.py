from django.shortcuts import render,HttpResponseRedirect,redirect
from .form import Userform,Sellerform,Productform
from .models import Product,User_mode,Seller_Model,Cart_model
from django.contrib.auth.decorators import login_required
from home import calc
# Create your views here.

@login_required()
def product_show(r):
    form = Product.objects.all()
    return render(r,'home/product_show.html',{'form':form})


# @login_required()
# def User_view(r,id):
#     form=Userform()
#     if r.method=="POST":
#         form=Userform(r.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/payment')
#     return render(r,'home/userform.html',{'form':form})
@login_required()
def Seller_view(r):
    form=Sellerform()
    if r.method=="POST":
        form=Sellerform(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
    return render(r,'home/Sellerform.html',{'form':form})


@login_required()
def Product_view(r):
    form=Productform()
    if r.method=="POST":
        form=Productform(r.POST,r.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productshow')
    return render(r,'home/Productform.html',{'form':form})

@login_required()
def Selection_View(r):
    return render(r,'home/selection.html')

def Home_view(r):
    form = Product.objects.all()
    return render(r, 'home/cards.html', {'form': form})
def login(r):
    return render(r,'registration/login.html')

def view(r):
    form = Product.objects.all()
    return render(r, 'home/product_view.html', {'form': form})


# def delete(r,id):
#     abc = Product.objects.get(id=id)
#     abc.delete()
#     return HttpResponseRedirect('/productshow')



def detail(r,id):
    form = Product.objects.get(id=id)
    return render(r,'product_detail.html',{'form':form})    #{'form':form}

def Cartview(r):
    Username=r.session['Username']
    product_id=r.GET.get('prod_id')
    product_name=product.objects.get(id=product_id)
    product=product.objects.filter(id=product_id)
    for p in product:
        image=p.product_image
        price=p.product_cost
        Cart(Username=Username,product=product_name,image=product_image,price=product_cost).save()
        return redirect(f"/detail/{product_id}")


# def payment(r):
#
#     return render(r,'home/payment_method.html')

@login_required
def User_view(r,id):
    obj=Product.objects.get(id=id)
    form=Userform()
    global det
    det={'id':obj.id}
    if r.method=="POST":

        det['qunt']=r.POST['quantity']
        det['cost']=r.POST['product_cost']

        print(qunt,cost,obj.id)
        # form=Userform(r.POST)
        # if form.is_valid():
        #     form.save()
        return HttpResponseRedirect(f"/payment/{obj.id}/")

    return render(r,'home/userform.html',{'form':obj,'ob':form})




def payment(r,id):
    obj=Product.objects.get(id=id)
    Total_cost=calc.total(det['qunt'],det['cost'])
    return render(r,'home/payment_method.html',{'obj':obj,'total':Total_cost})






