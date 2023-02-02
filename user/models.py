from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=10, null=True)
    image = models.ImageField(default="avatar.png", upload_to="Profile_Images")

    def __str__(self):
        return f"{self.staff.username}-Profile"
