import sys
import cv2
import argparse
import numpy as np


def contador(nameFile):
        img = cv2.imread(nameFile,0)

        img = cv2.medianBlur(img,1)
        for i in range(len(img[0])):
                for j in range(len(img)):
                        if(img[j][i]>220):
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

        #cv2.imwrite('save.jpg',img)
        numero=""
        y=0
        blanco=0
        negro=0
        x=len(img[0])-1
        ubicacion = 0

        for i in reversed(range(len(img))):
        	for j in range(len(img[0])):
        		if(img[i][j]>200):
        			blanco=1
        			ubicacion=i
        			break
        	if(blanco==1):
        		break
        ubicacion=ubicacion-5
        while(x>0):
                y=0
                if(img[ubicacion][x]>200):
                        blanco=1
                        negro=0
                        while(img[ubicacion][x]>200):
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
        #print(numero)
        #print(resultado)
        return resultado
