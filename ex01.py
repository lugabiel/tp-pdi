import numpy as np
import cv2
import time as time
#CARREGANDO IMAGEM
img = cv2.imread('GASTURA.jpg')


#TRANSFORMACOES
#inverte imagem
imgInv = ~img

#escala de cinza
imgCinz = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#transf. logaritmica
img1 = np.uint8(np.log1p(img))
limiar = 1
imgLog = cv2.threshold(img1,limiar, 255, cv2.THRESH_BINARY)[1]

#tranf. potencia
gamma = 5
imgG = np.power(img, gamma)
imgGamma = (1/imgG)




#SHOW IMAGES
#cv2.imshow('normal', img)
cv2.waitKey(0)

#cv2.imshow('cinza',imgCinz)
cv2.waitKey(0)

#cv2.imshow('invertida', imgInv)
cv2.waitKey(0)

#cv2.imshow('log', imgLog)
cv2.waitKey(0)

cv2.imshow('(potencia)', imgGamma)
cv2.waitKey(0)


