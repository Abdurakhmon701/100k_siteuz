from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
	username = models.CharField(max_length=50,unique=True)
	password = models.CharField(max_length=250)
	firstname = models.CharField(max_length=50,blank=True)
	lastname = models.CharField(max_length=50,blank=True)
	viloyat = models.CharField(max_length=50,blank=True)
	shahar = models.CharField(max_length=50,blank=True)
	manzil = models.CharField(max_length=100,blank=True)
	image = models.ImageField(upload_to='images/',blank=True)