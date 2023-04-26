from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .form import Userform,Sellerform,Productform
from .models import Usermode,Seller_Model,Customer1, Product_details,Cart1
from home import calc
from django.contrib import messages
from django.db.models import Q
from django.db import connection
myconn = connection.cursor()
name= ''
# Create your views here.
def SignUp1(r):
    obj=Customer1.objects.all()
    if r.method=='GET':
        return render(r,'home/Signup1.html')
    else:
        postdata=r.POST
        name=postdata.get('name')
        phone=postdata.get('phone')

        error_message=None
        value={
            'phone':phone,
            'name':name
        }

        customer=Customer1(name=name,
                          phone=phone)
        if(not name):
            error_message = "name is required"
        elif not phone:
            error_message = "phone No. is required"
        elif len(phone)<10 or len(phone)>10:
            error_message = "phone No. must be 10 digit"
        elif customer.isExists():
            error_message = "Account already Exist"
            value={
            'phone':phone,
            'name':name
        }


        if not error_message:
            messages.success(r,'Congratulation !! Register Successfull')
            customer.register()
            return redirect('/')
        else:
            data={
                'error':error_message,
                'value':value

            }
            return render(r,'home/Signup1.html',data)



def login(r):
    if r.method=='GET':
        return render(r,'home/login.html')
    else:
        phone=r.POST.get('phone')

        error_message=None
        value={
            'phone':int(phone)
        }


        customer=Customer1.objects.filter(phone=r.POST['phone'])
        if customer:
            r.session['phone']= int(phone)
            return redirect('/')
        else:
            error_message= "mobile No is Invalid !!"

            data={
                'error':error_message,
                'value':value
            }


        return render(r,'home/login.html',data)

def login_decor(f):
    try:
        def inner(r):
            if r.session.has_key('phone'):
                result = f(r) 
                return result
            else:
                return HttpResponseRedirect('/login')
        return inner
    except:
        def inner(r, id):
            if r.session.has_key('phone'):
                result = f(r, id) 
                return result
            else:
                return HttpResponseRedirect('/login')
        return inner

def logout(r):
    del r.session['phone']
    return redirect('/login') 
        
@login_decor
def product_show(r):
    if len(Product_details.objects.all()) != 0:
        form = Product_details.objects.filter(Seller_mob_no=r.session['phone'])
        return render(r,'home/product_show.html',{'form':form})

def Home_view(r):
    switch = 'login'
    name=''
    data = Product_details.objects.all()
    if r.session.has_key('phone'):
        data1 = myconn.execute(f"select * from home_Customer1 where phone = {r.session['phone']}")
        name = ''.join([i.name for i in data1])
        switch='logout'
    return render(r, 'home/cards.html',{'data':data, 'name':name, 'log':switch})
    


def Seller_view(r):
    form=Sellerform()
    if r.method=="POST":
        form=Sellerform(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
    return render(r,'home/Sellerform.html',{'form':form})
    

def delete(r,id):
    abc = Product_details.objects.get(id=id)
    abc.delete()
    return HttpResponseRedirect('/productshow')



def Product_view(r):
    form=Productform()
    if r.method=="POST":
        form=Productform(r.POST,r.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productshow')
    return render(r,'home/Productform.html',{'form':form,'num':int(r.session['phone'])})



def update(r,id):
    abc= Product_details.objects.get(id=id)
    if r.method=="POST":
        form=Productform(r.POST, r.FILES, instance=abc)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productshow')
    return render(r,'home/update.html',{'abc':abc})


@login_decor
def detail(r,id):
    totalitem=0
    form = Product_details.objects.get(id=id)
    Item_already_in_cart=False
    phone=r.session['phone']
    totalitem=len(Cart1.objects.filter(phone=phone))
    Item_already_in_cart=Cart1.objects.filter(Q(Product_brand=form.id) & Q(phone=phone)).exists()
    customer=Customer1.objects.filter(phone=phone)
    for c in customer:
        name=c.name
    data={
        'form':form,
        'Item_already_in_cart':Item_already_in_cart,
        'name':name,
        'totalitem':totalitem

    }
    if r.method=="POST":
        r.session['quant'] = r.POST['quant']
        
        return HttpResponseRedirect(f'/user/{form.id}')
    return render(r,'product_detail.html',data)    #{'form':form}

@login_decor
def User_view(r,id):
    obj=Product_details.objects.get(id=id)
    data={
        'obj':obj,
        'fetched_cost': obj.product_cost,
        'fetched_quant':r.session['quant'],
        'total': int(obj.product_cost)*int(r.session['quant'])
        }

    return render(r,'home/userform.html',data)


def Cartview(r):
    phone=r.session['phone']
    product_id=r.GET.get('prod_id')
    product_name=Product_details.objects.get(id=product_id)
    product=Product_details.objects.filter(id=product_id)
    print(product_name.id)
    for p in product:
        product_image=p.product_image
        product_cost= p.product_cost
        Cart1(
                id=product_id,
                phone=phone,
                Product_brand=product_name,
                product_image=product_image,
                product_cost=product_cost
              ).save()
        return redirect(f"/detail/{product_id}")
        

def show_add_to_cart(r):
    form=Cart1.objects.all()
    data = [] #list of dictionaries of data
    
    for i in form:
        result = myconn.execute(f"select * from home_Product_details where id={i.Product_brand_id}")
        for i in result:
            data.append(i)
            
    if r.method=="POST":
        if '' not in r.POST.getlist('qun'):
            qun = [int(i) for i in r.POST.getlist('qun')]
            var2 = r.POST.getlist('p_id')
            for i,j in enumerate(var2):
                data = myconn.execute(f"Select product_cost from Home_Product_details where id = {j}")
                if qun[i] != 0:
                    costs = [i for i in data]
                    total_cost = {j:[costs[0][0]*qun[i],qun[i]]}
                    myconn.execute(f"delete home_cart1 where id={j}" )
                    myconn.commit()
                    print(total_cost)
                    return HttpResponseRedirect("/success")
            
          
    return render(r,'home/show_cart.html',{'form':data})


def remove_cart(r,id):
    abc = Cart1.objects.get(id=id)
    abc.delete()
    return HttpResponseRedirect('/show_cart')
    
def success(r):
    
    

    return render(r, 'home/success.html')
    
    
    
    

