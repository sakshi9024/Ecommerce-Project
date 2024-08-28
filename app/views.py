from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from .models import Customer, Products , Cart, OrderPlaced  
from .forms import CustomerRegistrationForm , CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required   # for function based view --- restrict to view profile when user is logout 
from django.utils.decorators import method_decorator    # for class based view -------- restrict to view profile when user is logout



class ProductView(View):
  def get(self,request):
    topwear = Products.objects.filter(category='tw')
    bottomwear = Products.objects.filter(category='bw')
    mobile = Products.objects.filter(category='M')
    laptop = Products.objects.filter(category='L')
    return render(request,'app/home.html',{'topwear':topwear , 'bottomwear':bottomwear ,'mobile':mobile , 'laptop':laptop})
 
class ProductDetail(View):
  def get(self,request,id):
    product = Products.objects.get(id=id)
    item_already_in_cart = False
    item_already_in_cart = Cart.objects.filter(Q (products=product.id) & Q(user = request.user)).exists()
    return render(request,'app/productdetail.html',{'product':product, 'item_already_in_cart':item_already_in_cart}) 
 
class CustomerRegistration(View):
  def get(self,request):
    form = CustomerRegistrationForm()
    return render(request,'app/customerregistration.html',{'form':form})
  def post(self,request):
    form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
      messages.success(request,'Congratulation!! Registered Successfully')
      form.save()
    return render (request,'app/customerregistration.html',{'form':form})
  

def mobile(request,data=None):
  if data == None:
    mobiles = Products.objects.filter(category='M')
  elif data=='Redmi' or data=='Samsung':
      mobiles = Products.objects.filter(category='M').filter(brand=data)
  elif data == 'below':
      mobiles = Products.objects.filter(category='M').filter(discount_price__lt=10000)
  elif data == 'above':
      mobiles = Products.objects.filter(category='M').filter(discount_price__gt=10000)
  return render(request, 'app/mobile.html',{'mobiles':mobiles}) 

@method_decorator(login_required , name='dispatch')
class Profile(View):
  def get(self, request):
    form = CustomerProfileForm()
    return render(request,'app/profile.html',{'form': form, 'active':'btn-primary'})
    
  def post(self,request):
      form = CustomerProfileForm(request.POST)
      if form.is_valid():
        usr = request.user
        name = form.cleaned_data['name']
        locality = form.cleaned_data['locality']
        city = form.cleaned_data['city']
        state = form.cleaned_data['state']
        zipcode = form.cleaned_data['zipcode']
        reg = Customer(user=usr,name=name, locality=locality,city=city,state=state,zipcode=zipcode)
        reg.save()
        messages.success(request, "Congratulations!! profile updated successfully")
        return render(request,'app/profile.html',{'form':form , 'active': 'btn-primary'})
    
      return render(request,'app/profile.html',{'form': form})

  
@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add': add , 'active':'btn-primary' })
  
@login_required
def logouthandle(request):
    logout(request)
    return redirect('/')


@login_required
def add_to_cart(request):
   user=request.user
   product_id = request.POST['prod-id']
   print(product_id, "This is our product id")
   product = Products.objects.get(id =product_id)
   quantity = 1
   Cart(user=user,products=product,quantity=quantity).save()
   return redirect('/cart/')
   

@login_required
def show_cart(request):
  if request.user.is_authenticated:
    data = Cart.objects.filter(user=request.user)
    print(data)
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user==request.user]

    # cart_product= []
    # for p in Cart.objects.all():
    #   cart_product.append(p)

    # cart_product = Cart.objects.filter(user = request.user)

    if cart_product:
      for p in cart_product:
        tempamount = (p.quantity * p.products.discount_price)
        amount += tempamount
        totalamount = amount + shipping_amount
      return render(request,'app/add_to_cart.html',{'carts':data,'totalamount':totalamount , 'amount':amount})
    else:
      return render(request,'app/emptycart.html')
    
def plus_cart(request):
  if request.method=="GET":
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(products = prod_id) & Q(user = request.user))
    c.quantity += 1
    c.save()
    amount = 0.0
    shipping_amount =70.0
    cart_product = [p for p in Cart.objects.all() if p.user ==request.user] 
    for p in cart_product:
      tempamount = (p.quantity * p.products.discount_price )
      amount += tempamount 

    data ={
      'quantity' : c.quantity,
      'amount': amount,
      'totalamount': amount + shipping_amount
    }
    return JsonResponse(data) 
  
def minus_cart(request):
    if request.method=="GET":
      prod_id = request.GET['prod_id']
      c = Cart.objects.get(Q(products = prod_id) & Q(user = request.user))
      c.quantity -= 1
      c.save()
      amount = 0.0
      shipping_amount =70.0
      cart_product = [p for p in Cart.objects.all() if p.user ==request.user] 
      for p in cart_product:
        tempamount = (p.quantity * p.products.discount_price )
        amount += tempamount 

      data ={
        'quantity' : c.quantity,
        'amount': amount,
        'totalamount': amount + shipping_amount 
      }
      return JsonResponse(data) 

def remove_cart(request):
    if request.method=="GET":
      prod_id = request.GET['prod_id']
      c = Cart.objects.get(Q(products = prod_id) & Q(user = request.user))
      c.quantity -= 1
      c.delete()
      amount = 0.0
      shipping_amount =70.0
      cart_product = [p for p in Cart.objects.all() if p.user ==request.user] 
      for p in cart_product:
        tempamount = (p.quantity * p.products.discount_price )
        amount += tempamount 

      data ={
        'amount': amount,
        'totalamount': amount + shipping_amount 
      }
      return JsonResponse(data) 



def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required
def orders(request):
 op = OrderPlaced.objects.filter(user=request.user)
 return render(request, 'app/orders.html',{'order_placed':op})






  

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')


@login_required
def checkout(request):
  user = request.user
  add =  Customer.objects.filter(user=user)
  cart_items = Cart.objects.filter(user=user)
  amount = 0.0
  shipping = 70.0
  cart_product = [p for p in Cart.objects.all() if p.user == user] 
  if cart_product:
    for p in cart_product:
      tempamount = (p.quantity * p.products.discount_price)
      amount += tempamount
    totalamount = amount + shipping 
  return render(request,'app/checkout.html',{'add':add,'cart_items':cart_items,'totalamount':totalamount})
  
def payment_done(request):
  if request.method=="GET":
    user = request.user
    custid = request.GET['custid']
    customer = Customer.objects.get(id = custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
      OrderPlaced(user=user , product= c.products , customer=customer, quantity = c.quantity ).save()
      c.delete()
    return redirect("orders")  


