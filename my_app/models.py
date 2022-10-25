from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=200)
	category_name = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name

class HomePageModel(models.Model):
	zagolovok = models.CharField(max_length = 200)
	opisaniye = models.TextField()
	tsena = models.CharField(max_length = 20)
	foto = models.ImageField(upload_to = 'images/')
	category = models.ForeignKey(Category,null = True,on_delete=models.SET_NULL)

	def __str__(self):
		return self.zagolovok
# Create your models here.
