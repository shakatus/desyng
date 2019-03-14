import sys
import cv2
import argparse
import numpy as np

#print("This is the name of the script: "+ sys.argv[1])

img = cv2.imread(sys.argv[1],0)

img = cv2.medianBlur(img,1)
for i in range(len(img[0])):
        for j in range(len(img)):
                if(img[j][i]>220):
                        img[j][i]=255
                else:
                        img[j][i]=0

posx1=0
posx2=0
#cv2.imwrite('save.jpg',img)
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
#cv2.imwrite('save.jpg', img)
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

cv2.imwrite('save.jpg',img)
numero=""
y=0
blanco=0
negro=0
x=len(img[0])-1
#print(int(dist/2))
ubicacion = 0



for i in reversed(range(len(img))):
	for j in range(len(img[0])):
		if(img[i][j]>200):
			blanco=1
			ubicacion=i
			break
	if(blanco==1):
		break
ubicacion=ubicacion-50
print(ubicacion)
#ubicacion=ubicacion+5
#print(ubicacion)
#ubicacion = len(img)-(int(dist/1.5))
listaNumeros = []
while(x>0):
	if(img[0][x]>200):
		y=0
		while(img[0][x]>200):
			y+=1
			x-=1
		listaNumeros.append(y)
	else:
		x-=1

minx=min(listaNumeros)
maxx=max(listaNumeros)
#print("max "+str(max(listaNumeros)))
x=len(img[0])-1
negro = minx*1.2
binario = ""
while(x>0):
	if(img[0][x]>200):
		y=0
		while(img[0][x]>200):
			y+=1
			x-=1
		print("blanco "+str(y))
		binario = "1"+binario
	else:
		y=0
		while(img[0][x]<=200):
			y+=1
			x-=1
		if(y>minx):
			for t in range(int(y/negro)):
				print("negro "+str(y))
				binario="0"+binario

print(binario)
print(int(binario,2))
"""
x=len(img[0])-1
while(x>0):
        y=0
        if(img[ubicacion][x]>200):
                blanco=1
                negro=0
                while(img[ubicacion][x]>200):
                        x=x-1
                        y=y+1
                        if(x==1 or y>=minx):
                                break
                if (y>=minx and y<=maxx):
                        numero="1"+numero
                        y=0
        else:
                negro=1
                blanco=0
                while(img[ubicacion][x]<200):
                        x=x-1
                        y=y+1
                        if(x==1 or y>=minx):
                                break
                if (y>=minx and y<=maxx):
                        numero="0"+numero
                        y=0
        x=x-1

resultado = int(numero,2)
print(numero)
#print(resultado)
print(resultado)
"""
