from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .form import Userform,Sellerform,Productform
from .models import Usermode,Seller_Model,User_Model, Product_details,Cart1,sales_detailss
from home import calc
from django.contrib import messages
from django.db.models import Q
from django.db import connection
from datetime import date
from itertools import chain#to join orm querysets
myconn = connection.cursor()
username= ''
switch = 'logout'
# Create your views here.
def SignUp1(r):
    obj=User_Model.objects.all()
    if r.method=='GET':
        return render(r,'home/Signup1.html')
    else:
        postdata=r.POST
        username=postdata.get('name')
        phone=postdata.get('phone')
        password=postdata.get('password')
        email_id=postdata.get('email_id')
        address_field=postdata.get('address_field')
        dob=postdata.get('dob')

        error_message=None
        value={
            'phone':phone,
            'username':username,
            'password':password,
            'email_id':email_id,
            'address_field':address_field,
            'dob':dob
        }

        customer=User_Model(username=username,password=password,email_id=email_id,address_field=address_field,
                          dob=dob,phone=phone)
        if(not username):
            error_message = "username is required"
        elif not phone:
            error_message = "phone No. is required"
        elif len(phone)!=10:
            error_message = "phone No. must be 10 digit"
        elif(not password):
            error_message = "Password is required"
        elif len(password)<8:
            error_message = "Password length is required"
        elif not email_id:
            error_message = "Email is required"
        elif not address_field:
            error_message = "Address is required"
        elif not dob:
            error_message = "Date Of Birth is required"
        elif '@' not in email_id or not email_id.endswith('.com'):
            error_message = "Email is invalid"
        elif customer.isExists():
            error_message = "Account already Exist"
            value={
            'phone':phone,
            'username':username,
            'password':password,
            'email_id':email_id,
            'address_field':address_field,
            'dob':dob
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
        password=r.POST.get('password')

        error_message=None
        value={
            'phone':int(phone),
            'password':password
        }


        customer=User_Model.objects.filter(phone=r.POST['phone'])
        if customer:
            passs = myconn.execute('select password from home_User_Model where phone = {}'.format(r.POST['phone']))
            for i in passs:
                if i[0] == r.POST['password']:    
                    r.session['phone']= int(phone)
                    return redirect('/')
            else:
                error_message= "Password is Invalid !!"

                data={
                    'error':error_message,
                    'value':value
                }
        else:
            error_message= "mobile No is Invalid !!"

            data={
                'error':error_message,
                'value':value
            }


        return render(r,'home/login.html',data)

def login_decor(f):
    def inner(r):
        if r.session.has_key('phone'):
            result = f(r)
            switch = 'logout'
            
            return result
        else:
            return HttpResponseRedirect('/login')
    return inner

def login_decor_id(f):    
    def inner(r, id):
        if r.session.has_key('phone'):
            result = f(r, id)
            switch = 'logout' 
            return result
        else:
            return HttpResponseRedirect('/login')
    return inner


def logout(r):
    del r.session['phone']
    return redirect('/login') 
        
@login_decor
def product_show(r):
    form = Product_details.objects.filter(Seller_mob_no=r.session['phone'])
    if len(form) != 0:
        user_name = ''.join([i.username for i in User_Model.objects.filter(phone=r.session['phone'])])
        return render(r,'home/product_show.html',{'form':form,'username':user_name, 'log':switch})

def Home_view(r):
    switch = 'login'
    username=''
    #data = Product_details.objects.order_by('-product_cost')[:4]
    data = Product_details.objects.all()
    if r.session.has_key('phone'):
        data1 = myconn.execute(f"select * from home_User_Model where phone = {r.session['phone']}")
        username = ''.join([i.username for i in data1])
        switch='logout'
    return render(r, 'home/cards.html',{'data':data, 'username':username, 'log':switch})
    


@login_decor
def Seller_view(r):
    form=Sellerform()
    if r.method=="POST":
        form=Sellerform(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
    return render(r,'home/Sellerform.html',{'form':form, 'log':switch})
    

@login_decor
def delete(r,id):
    abc = Product_details.objects.get(id=id)
    abc.delete()
    return HttpResponseRedirect('/productshow')



@login_decor
def Product_view(r):
    form=Productform()
    if r.method=="POST":
        form=Productform(r.POST,r.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productshow')
    return render(r,'home/Productform.html',{'form':form,'num':int(r.session['phone']),'log':switch})



@login_decor
def update(r,id):
    abc= Product_details.objects.get(id=id)
    if r.method=="POST":
        form=Productform(r.POST, r.FILES, instance=abc)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productshow')
    return render(r,'home/update.html',{'abc':abc, 'log':switch})

@login_decor_id
def detail(r,id):
    totalitem=0
    form = Product_details.objects.get(id=id)
    Item_already_in_cart=False
    phone=r.session['phone']
    totalitem=len(Cart1.objects.filter(phone=phone))
    Item_already_in_cart=Cart1.objects.filter(Q(Product_brand=form.id) & Q(phone=phone)).exists()
    customer=User_Model.objects.filter(phone=phone)
    for c in customer:
        username=c.username
    data={
        'form':form,
        'Item_already_in_cart':Item_already_in_cart,
        'username':username,
        'totalitem':totalitem,
        'log':switch

    }
    if r.method=="POST":
        r.session['quant'] = r.POST['quant']
        
        return HttpResponseRedirect(f'/user/{form.id}')
    return render(r,'product_detail.html',data)    

@login_decor
def Cartview(r):
    phone=r.session['phone']
    product_id=r.GET.get('prod_id')
    username = ''.join([i.username for i in User_Model.objects.filter(phone=r.session['phone'])])
    product_name=Product_details.objects.get(id=product_id)
    product=Product_details.objects.filter(id=product_id)
    
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
        
@login_decor
def show_add_to_cart(r):
    form=Cart1.objects.filter(phone=r.session['phone'])
    user_name = ''.join([i.username for i in User_Model.objects.filter(phone=r.session['phone'])])
    data = [] #list of dictionaries of data
    print(username)
    for i in form:
        result = myconn.execute(f"select * from home_Product_details where id={i.Product_brand_id}")
        for i in result:
            data.append(i)
            
    if r.method=="POST":
        final_cost = 0
        total_quant = 0 
        payment_lists = []
        if '' not in r.POST.getlist('qun'):
            qun = [int(i) for i in r.POST.getlist('qun')]
            var2 = r.POST.getlist('p_id')
            for i,j in enumerate(var2):
                data = myconn.execute(f"Select product_cost from Home_Product_details where id = {j}")
                if qun[i] != 0:
                    costs = [i for i in data]
                    payment_details = {j:qun[i]}
                    payment_lists.append(payment_details)
                    myconn.execute(f"delete home_cart1 where id={j}" )
                    myconn.commit()
                    final_cost += costs[0][0]*qun[i]
                    total_quant += qun[i]
                    

        calculated_data={
        'fetched_quant':total_quant,
        'total': final_cost
        }
        r.session['cal_data'] = payment_lists
    
        
        return render(r, 'home/payments_method.html', calculated_data) 
    cart_data = {
            'form':data, 
            'log':switch, 
            'username':user_name
    }
    return render(r,'home/show_cart.html',cart_data)


@login_decor
def remove_cart(r,id):
    abc = Cart1.objects.get(id=id)
    abc.delete()
    return HttpResponseRedirect('/show_cart')
   


@login_decor      
def success(r):
    calculated_data = r.session['cal_data'] 
    print(calculated_data)
    # cal_data= [
        # {'1': 3}, 
        # {'2': 2}, 
        # {'3': 1}
    # ]
    
    for product_dict_keys in calculated_data:
        print(product_dict_keys)
        for prd_id, Quant in product_dict_keys.items():
            print("values", rec_no, product_id)
            
            # myconn.execute(f"delete home_cart1 where id={product_id}" )   
            # myconn.commit()
            
        # sales_detailss(
            # record_date=date.today(),
            # buyer_id=r.session['phone'],
            # product_id=product_id,
            # prd_quant=calculated_data[rec_no].get(product_id) 
            # ).save()
    del r.session['cal_data']      
            
    return render(r, 'home/success.html') 

@login_decor 
def buy_history(r):
    buy_data = sales_detailss.objects.filter(buyer_id = r.session['phone'])
    buy_prd = [Product_details.objects.filter(id = i.product_id) for i in buy_data]
    user_name = ''.join([i.username for i in User_Model.objects.filter(phone=r.session['phone'])])
    
    history_data = {
            'form':buy_prd,
            'dates':[i.record_date for i in buy_data],
            'username':user_name       
    }
    
    
    #result_list = list(chain(buy_prd, buy_data))
    
    return render(r, 'home/buy_history.html',history_data)

    
    
    
def search(r):
    switch='login'
    totalitem=0
    query=r.GET.get('query')
    search1=Product_details.objects.filter(Q(Product_brand__contains=query) | Q(product_name__contains=query) | Q(Product_category__contains=query))
    data={          
        'search1':search1,
        'query':query, 
        'log':switch
    }    
    
    if r.session.has_key('phone'):
        switch='logout'
        totalitem=len(Cart1.objects.filter(phone=r.session['phone']))
        customer=User_Model.objects.filter(phone=r.session['phone'])
        for c in customer:
            data['username']=c.username
            data['log']=switch
                        
    return render(r,'home/search.html',data)