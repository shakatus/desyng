from django.db import models

# Create your models here.
class Point(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField()
	longitud = models.CharField(max_length=50)
	latitud = models.CharField(max_length=50)
	contact = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	phone	= models.CharField(max_length=20)
	codigo	= models.CharField(max_length=100, unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)

class Scale(models.Model):
	location = models.CharField(max_length=250)
	description = models.TextField()
	longitud = models.CharField(max_length=50, default="")
	latitud = models.CharField(max_length=50, default="")
	point = models.IntegerField()
	codigo	= models.CharField(max_length=100, unique = True, null=True )
	timestamp = models.DateTimeField(auto_now_add=True)

class Raise(models.Model):
	scale = models.IntegerField()
	quantity	= models.IntegerField()
	amount  	= models.DecimalField(max_digits=30, decimal_places=15)
	base64		= models.TextField(default="-")
	codigo	= models.CharField(max_length=100, null=True)
	timestamp   = models.DateTimeField(auto_now_add=True)

