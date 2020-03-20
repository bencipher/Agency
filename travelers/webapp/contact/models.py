from django.db import models

# Create your models here.
class Contact(models.Model):
    # id: int
    # firstname: str
    # lastname: str
    # email: str
    # subject: str 
    # image = models.ImageField(upload_to='photos')
    # price = models.IntegerField()
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=100)
    message = models.TextField()

