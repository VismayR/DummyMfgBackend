from django.db import models

# Create your models here.
# declaring a Student Model   

class UsersData(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    userName = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    postcode = models.IntegerField(default=0)
    country = models.CharField(max_length =10)
    image_url = models.ImageField(upload_to='images/', blank=True, null=True)