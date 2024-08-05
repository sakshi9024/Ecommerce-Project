from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","user","name","locality","city","zipcode","state"]


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","title","selling_price","discount_price","description","brand","image","category"]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id","user","products","quantity"]

@admin.register(Order_Details)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id","user","customer","product","quantity","ordered_date","status"]
