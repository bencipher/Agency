from django.db import models

# Create your models here.
class Mission(models.Model):
    # id: int
    # price: int
    # image: str
    # location: 
    image = models.ImageField(upload_to='photos')
    price = models.IntegerField()
    location = models.CharField(max_length=100)
