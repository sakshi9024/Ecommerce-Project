from django.shortcuts import render
from django.views import View
from .models import Customer, Products , Cart, Order_Details   
from .forms import CustomerRegistrationForm 
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
    return render (request,'customerregistration.html',{'form':form})


# def home(request):
#  return render(request, 'app/home.html')

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
  if data == None:
    mobiles = Products.objects.filter(category='M')
  elif data=='Lenovo' or data=='Samsung':
      mobiles = Products.objects.filter(category='M').filter(brand=data)
  elif data == 'below':
      mobiles = Products.objects.filter(category='M').filter(discount_price__lt=10000)
    
  elif data == 'above':
      mobiles = Products.objects.filter(category='M').filter(discount_price__gt=10000)
  return render(request, 'app/mobile.html',{'mobiles':mobiles}) 


def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
