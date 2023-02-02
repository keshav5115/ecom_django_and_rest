from django import forms
from .models import Product, Customer, Order


class ProductForm(forms.ModelForm):
    class Meta:

        model = Product
        fields = ["name", "category", "quantity"]


class CustomerForm(forms.ModelForm):
    class Meta:

        model = Customer
        fields = "__all__"


class OrderForm(forms.ModelForm):
    class Meta:

        model = Order
        fields = ["product", "order_quantity", "price"]
