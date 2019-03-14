from django.shortcuts import render
from scales.models import *

def results(request, point_id):
#	Scale = 0
	#if point_id>0:
	Scales = Scale.objects.all().filter(point = point_id)
	#Scales = Scale.objects.raw('select * from scales_scale '+
#				'join scales_raise on scales_scale.id = scales_raise.scale_id '+
#				'where scales_scale.point_id='+str(point_id))
	#Points = Point.objects.all()
	return render(request, 'index.html',{'scales':Scales})

# Create your views here.
