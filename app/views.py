from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from .models import Customer, Products , Cart, Order_Details   
from .forms import CustomerRegistrationForm , CustomerProfileForm
from django.contrib import messages



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
    return render(request,'app/productdetail.html',{'product':product}) 
 
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


# def home(request):
#  return render(request, 'app/home.html')

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

def add_to_cart(request):
   user=request.user
   product_id = request.POST['prod-id']
   print(product_id, "This is our product id")
   product = Products.objects.get(id =product_id)
   quantity = 1
   Cart(user=user,products=product,quantity=quantity).save()
   return redirect('/cart/')
   


def show_cart(request):
  data = Cart.objects.filter(user=request.user)
  return render(request,'app/add_to_cart.html',{'carts':data})

def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html',{'add': add , 'active':'btn-primary' })

def orders(request):
 return render(request, 'app/orders.html')


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

  

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

def logouthandle(request):
  logout(request)
  return redirect('/')

def checkout(request):
 return render(request, 'app/checkout.html')




