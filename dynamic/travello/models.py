from django.db import models

# Create your models here.
class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    des = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Navbar:
    call:str
    phone:str
    