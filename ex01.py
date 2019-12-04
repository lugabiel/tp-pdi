import numpy as np
import cv2



#CARREGANDO IMAGEM
img  = cv2.imread('GASTURA.jpg')
img2 = cv2.imread('BYELO.jpg')


#TRANSFORMACOES
#Q1 - inverte imagem
imgInv  = ~img

#escala de cinza
imgCinz = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Q2 - transf. logaritmica
img1 = np.uint8(np.log1p(img))
limiar = 1
imgLog  = cv2.threshold(img1,limiar, 255, cv2.THRESH_BINARY)[1]

#Q3 - transf. potencia (figura1)
gamma = 5
imgG = np.power(img, gamma)


#Q4 - transf. com curva generica (figura2)
def pixelVal(pix, r1,s1,r2,s2):
    if (0 <= pix and pix <=r1):
        return (s1/r1)*pix
    elif (r1 < pix and pix <= r2):
        return ((s2-s1)/(r2-r1))*(pix - r1) + s1
    else:
        return ((255 - s2)/(255 - r2))*(pix - r2) + s2

'''vetoriando funcao para avaliar cada pixel'''
pixelVal_vec = np.vectorize(pixelVal)

#Q5 - A
r1 = 10
s1 = 20
r2 = 200
s2 = 21

#cv2.imshow('curva generica', imgAlarg1)
imgAlarg1 = pixelVal_vec(img,r1,s1,r2,s2)
cv2.waitKey(0)

#Q5 - B 
m = 130
r1 = r2 = m
s1 = 254
#r2 = 100
s2 = 255


imgAlarg2 = pixelVal_vec(img,r1,s1,r2,s2)
#cv2.imshow('curva generica', imgAlarg2)
cv2.waitKey(0)


#Q6 - transf. com curva (figura3) - filtro passa faixa de intensidade
def passaFaixa(pix, A,B):
    if (A <= pix and pix >= B):
        return 0.6*pix
    else:
        return 0.1*pix
A = 254
B = 256

'''vetorizando funcao'''
passaFaixa = np.vectorize(passaFaixa)

'''aplicando filtro passa-faixa de intensidade'''
imgFaixa = passaFaixa(img,A,B)

#Q7 - transf. com curva (figura4) - filtro passa faixa de intensidade
def realceFaixa(pix, A,B):
    if (A <= pix and pix >= B):
        return 0.8*pix
    else:
        return 3.0*pix
A2 = 0
B2 = 50

'''vetorizando funcao'''
realceFaixa = np.vectorize(realceFaixa)

'''aplicando filtro realca-faixa de intensidade'''
imgRealce = realceFaixa(img,A,B)



#SHOW IMAGES
#cv2.imwrite('normal', img)
cv2.waitKey(0)

#cv2.imwrite('cinza',imgCinz)
cv2.waitKey(0)

#cv2.imwrite('invertidaBYELO.jpg', imgInv)
cv2.waitKey(0)

#cv2.imwrite('logBYELO.jpg', imgLog)
cv2.waitKey(0)

#cv2.imwrite('gammaBYELO.jpg', imgG)
cv2.waitKey(0)

#cv2.imwrite('curva_genericaABYELO.jpg', imgAlarg1)
cv2.imshow('curva_genericaBBYELO.jpg', imgAlarg2)
cv2.waitKey(0)

#cv2.imshow('passa-faixa', imgFaixa)
#cv2.imwrite('passa_faixaBYELO.jpg', imgFaixa)
cv2.waitKey(0)

#cv2.imshow('realce', imgRealce)
cv2.imwrite('realce.jpg', imgRealce)





#FUNCAO P/ ENCONTRAR PIXEL MAIS INTENSO
'''
x = 0
y = 0
canal = 0
coordenada = (0,0,0)
intensidade = 0
while(x < 610):     
    while(y < 610):
        while(canal < 3):
            b,g,r = cv2.split(img[x,y,canal])
            coordenadasNova = (x,y,canal)
            intensidadeNova = b + g + r
            if intensidadeNova > intensidade:
                intensidade = intensidadeNova
                coordenada = coordenadaNova
                print(intensidade, coordenada)
            canal = canal + 1
        y = y +1
    x = x + 1
'''
