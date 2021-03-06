import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Point(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField()
	longitud = models.CharField(max_length=50)
	latitud = models.CharField(max_length=50)
	contact = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	phone	= models.CharField(max_length=20)
	codigo	= models.CharField(max_length=100, null=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Scale(models.Model):
	location = models.CharField(max_length=250)
	description = models.TextField()
	longitud = models.CharField(max_length=50, default="")
	latitud = models.CharField(max_length=50, default="")
#	point = models.IntegerField()
	point = models.ForeignKey(Point, on_delete=models.CASCADE)
	codigo	= models.CharField(max_length=100, null=True )
	timestamp = models.DateTimeField(auto_now_add=True, editable=True)

	def __str__(self):
		return self.location

class Date(models.Model):
	fecha           =  models.DateTimeField(default=timezone.now, editable=True)
	point           =  models.ForeignKey(Point, on_delete=models.DO_NOTHING, null=True)
	
	def __str__ (self) :
		return str(self.fecha)


class Raise(models.Model):
	#scale = models.IntegerField()
	scale		= models.ForeignKey(Scale, on_delete=models.DO_NOTHING, null=True)
	quantity	= models.IntegerField()
	amount  	= models.DecimalField(max_digits=30, decimal_places=15)
	base64		= models.TextField(default="-")
	codigo	= models.CharField(max_length=100,null=True, unique=True)
	timestamp   = models.DateTimeField(default=timezone.now)
	date		= models.ForeignKey(Date,on_delete=models.DO_NOTHING, null=True)

	def __str__(self):
		return str(self.timestamp)

