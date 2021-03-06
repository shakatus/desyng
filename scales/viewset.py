from rest_framework.decorators import action
from rest_framework import viewsets
from scales.serializers import PointSerializer, ScaleSerializer, RaiseSerializer
from scales.models import Point, Scale, Raise
import logging
import cv2
import argparse
import numpy as np
import base64
import script
from io import StringIO

logger = logging.getLogger(__name__)

class PointViewSets(viewsets.ModelViewSet):
	queryset = Point.objects.all()
	serializer_class = PointSerializer

class ScaleViewSets(viewsets.ModelViewSet):
	queryset = Scale.objects.all()
	serializer_class = ScaleSerializer

class RaiseViewSets(viewsets.ModelViewSet):
	queryset = Raise.objects.all()
	serializer_class = RaiseSerializer


	def perform_create(self, serializer):

		data = self.request.data
		device = serializer.save()
		Owner(device)

def Owner(device):
	#device.amount = 12
	#device.save()
	scale=device.codigo.split("_")[0]
	bascula = Scale.objects.get(id = scale)
	device.scale=bascula
#	device.save()

	q = Raise.objects.all().filter(scale = bascula.id).order_by('-timestamp')[:2]
	if (len(q)==2):
		ultimo=q[1].quantity
	else:
		ultimo=0
	try:
		filename = "imagen_"+str(device.id)+".png"
		buf_decode = base64.b64decode(device.base64)
		with open(filename, 'wb') as f:
			f.write(buf_decode)
		f.close()
		resultado = 0
		resultado = script.contador(filename)
		device.quantity = resultado
		device.amount   = 0.25*((resultado-ultimo)%65535)
	except Exception  as e:
		device.base64 = str(e)

	device.save()
#	buf_decode = base64.b64decode(device.base64)
#+str(device.id)
#	filename = 'image'+device.id+'.jpg'  # I assume you have a way of picking unique filenames
#	with open(filename, 'wb') as f:
#		f.write(buf_decode)
"""
	img = cv2.imread(filename,0)

	img = cv2.medianBlur(img,1)
	for i in range(len(img[0])):    
		for j in range(len(img)):
			if(img[j][i]>220)|:
				img[j][i]=255
			else:
				img[j][i]=0

	posx1=0
	posx2=0

	for j in reversed(range(len(img))):
		if (posx1!=0):
			break
		for i in range(len(img[0])):
			if(img[j][i]>200):
				posx1=j
				break

	for j in (range(len(img))):
		if (posx2!=0):
			break
		for i in range(len(img[0])):
			if(img[j][i]>200):
				posx2=j
				break

	dist = abs(posx1-posx2)/9
	blanco=0
	cv2.imwrite('save.jpg', img)
	for i in range(len(img[0])):
		blanco=0
		for j in reversed(range(len(img))):
			if(j<posx1 and j>(posx1-dist)):
				if(img[j][i]>200):
					blanco=1
			if(blanco==1):
				img[j][i]=255
			else:
				img[j][i]=0

	for i in range(len(img[0])):
		blanco=0
		for j in (range(len(img))):
			if(img[j][i]>200):
				blanco=1
			if(blanco==1):
				img[j][i]=255
			else:
				img[j][i]=0                


	numero=""
	y=0
	blanco=0
	negro=0
	x=len(img[0])-1
	
	ubicacion = len(img)-(int(dist/2))

	while(x>0):
		y=0
		if(img[ubicacion][x]>200):
			blanco=1
			negro=0
			while(img[ubiacion][x]>200):
				x=x-1
				y=y+1
				if(x==1 or y>=20):
					break
			if (y>10 and y<=25):
				numero="1"+numero
				y=0
		else:
			negro=1
			blanco=0
			while(img[ubicacion][x]<200):
				x=x-1
				y=y+1
				if(x==1 or y>=20):
					break
			if (y>10 and y<=25):
				numero="0"+numero
				y=0
		x=x-1

	resultado = int(numero,2)	
	device.quantity= resultado
	device.amount  = 0
	device.save()
	logger.error(device.quantity)





"""
	#device.quantity=10
	#device.save()
	#logger.error(device.quantity)
	
