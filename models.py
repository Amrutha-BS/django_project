from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=300)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField(max_length=1000,null=True)
    date= models.DateTimeField(auto_now_add=True)
    price=models.IntegerField()
    seller_fname=models.CharField(max_length=100,null=True)
    seller_lname=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=200)
    

class contact_Us(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    msg=models.TextField(max_length=700)
    date= models.DateTimeField(auto_now_add=True)
    
