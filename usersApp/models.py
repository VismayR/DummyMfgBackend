from django.db import models

# Create your models here.
STATE_CHOICES = (
    ("UK", "UK"),
    ("Argentina", "Argentina"),
    ("portugal", "portugal"),
    ("India", "India"),
)
  
# declaring a Student Model      

class UsersData(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    userName = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    postcode = models.IntegerField(default=0)
    country = models.CharField(
        max_length = 9,
        choices = STATE_CHOICES,
        default = 'UK'
        )