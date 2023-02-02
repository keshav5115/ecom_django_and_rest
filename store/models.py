from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    CATEGORY = [
        ("Stationary", "Stationary"),
        ("Electronics", "Electronics"),
        ("Food", "Food"),
    ]
    name = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.name} = {self.quantity}"


class Customer(models.Model):

    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
    total = models.PositiveIntegerField(editable=False, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} ordered by {self.staff.username}"
