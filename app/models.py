from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator 

State_Choice = (  

('Andhra Pradesh' ,'Andhra Pradesh'),
('Arunachal Pradesh', 'Arunachal Pradesh'),
('Assam', 'Assam'),
('Bihar', 'Bihar'),
('Chhattisgarh', 'Chhattisgarh'),
('Goa', 'Goa'),
('Gujarat', 'Gujarat'),
('Haryana', 'Haryana'),
('Himachal Pradesh', 'Himachal Pradesh'),
('Jharkhand', 'Jharkhand'),
('Karnataka', 'Karnataka'),
('Kerala', 'Kerala'),
('Madhya Pradesh', 'Madhya Pradesh'),
('Maharashtra', 'Maharashtra'),
('Manipur', 'Manipur'),
('Meghalaya', 'Meghalaya'),
('Mizoram', 'Mizoram'),
('Nagaland', 'Nagaland'),
('Odisha', 'Odisha'),
('Punjab', 'Punjab'),
('Rajasthan', 'Rajasthan'),
('Sikkim', 'Sikkim'),
('Tamil Nadu', 'Tamil Nadu'),
('Telangana', 'Telangana'),
('Tripura', 'Tripura'),
('Uttar Pradesh', 'Uttar Pradesh'),
('Uttarakhand', 'Uttarakhand'),
('West Bengal', 'West Bengal')
)

class Customer(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=State_Choice, max_length=50)

    def __str__(self):
       return str(self.id)


Product_Category = (

    ('M','mobile'),
    ('L','laptop'),
    ('tw','topwear'),
    ('bw','bottomwear')
)

class Products(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.IntegerField()
    discount_price = models.IntegerField()
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=50)
    image = models.ImageField(upload_to='productimg')
    category = models.CharField(choices=Product_Category,max_length=2)

    def __str__(self):
       return str(self.title)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity =  models.IntegerField()

    def __str__(self):
       return str(self.id)


Order_Status = (
    ('Accepted','Accepted'),
    ('packed','packed'),
    ('On_the_way','On_the_way'),
    ('delivered','delivered'),
    ('cancel','cancel'),
   
)

class Order_Details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Order_Status, default='Pending', max_length=50)

    def __str__(self):
        return(self.id)


