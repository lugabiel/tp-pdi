import cv2
import numpy as np
from matplotlib import pyplot as plt

#CARREGANDO IMAGEM
img  = cv2.imread('GASTURAcinza.jpg')
img2 = cv2.imread('BYELOcinza.jpg')
img3 = cv2.imread('BYELO.jpg')

#escala de cinza
#imgCinz  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imwrite('GASTURAcinza.jpg',imgCinz)


#Q8

# reads an input image 
img = cv2.imread('GASTURA.jpg',0) 
  
# find frequency of pixels in range 0-255 
#histr  = cv2.equalizeHist(img)
#plt.hist(histr)
#plt.show()

#plt.hist(img.ravel(),256,[0,256]); plt.show()


#plt.hist(img2.ravel(),256,[0,256]); plt.show()


'''
cv2.imshow('histGASTURA', histr)
cv2.imshow('hello', histr2)
cv2.waitKey(0)
'''
#10 
n = 2
sharpKernel3X3 = np.array([[-1,-1,-1],
                           [-1,9,-1],
                           [-1,-1,-1]])
media5X5kernel =       np.array([[ 1, 1, 2, 1, 1],
                           [ 1, 2, 4, 2, 1],
                           [ 2, 4, 8, 4, 2],
                           [ 1, 2, 4, 2, 1],
                           [ 1, 1, 2, 1, 1]])
media3X3kernel =       np.array([[ 1, 2, 1],
                           [ 2, 4, 2],
                           [ 1, 2, 1]])

sharpKernel5X5 = np.array([[-1,-1,-1,-1,-1],
                           [-1, 1, 1, 1,-1],
                           [-1, 1, 9, 1,-1],
                           [-1, 1, 1, 1,-1],
                           [-1,-1,-1,-1,-1]])
#convolucao com kernel n x n
sharp = cv2.filter2D(img,-1,sharpKernel5X5,borderType=cv2.BORDER_CONSTANT)
sharp2 = cv2.filter2D(img3,-1,sharpKernel5X5,borderType=cv2.BORDER_CONSTANT)
cv2.imwrite('sharp5x5.jpg', sharp)
cv2.imwrite('sharpBYELO5x5.jpg', sharp2)

media = cv2.filter2D(img,-1,sharpKernel5X5,borderType=cv2.BORDER_CONSTANT)
media2 = cv2.filter2D(img2,-1,sharpKernel5X5,borderType=cv2.BORDER_CONSTANT)

cv2.imwrite('media5x5.jpg',media)
cv2.imwrite('mediaBYELO5x5.jpg',media2)
