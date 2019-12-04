import cv2
import numpy as np

#CARREGANDO IMAGEM
img  = cv2.imread('img.jpg')
img2 = cv2.imread('BYELOcinza.jpg')

#escala de cinza
imgCinz  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Q10
'''kernel de agucamento'''
sharpKernel3X3 = np.array([[-1,-1,-1],
                           [-1, 9,-1],
                           [-1,-1,-1]])

sharpKernel5X5 = np.array([[-1,-1,-1,-1,-1],
                           [-1, 1, 1, 1,-1],
                           [-1, 1, 9, 1,-1],
                           [-1, 1, 1, 1,-1],
                           [-1,-1,-1,-1,-1]])
'''kernel de media'''
media5X5kernel = np.array([[ 1, 1, 2, 1, 1],
                           [ 1, 2, 4, 2, 1],
                           [ 2, 4, 8, 4, 2],
                           [ 1, 2, 4, 2, 1],
                           [ 1, 1, 2, 1, 1]])

media3X3kernel = np.array([[ 1, 2, 1],
                           [ 2, 4, 2],
                           [ 1, 2, 1]])


#convolucao com kernel n x n

sharp = cv2.filter2D(img,-1,sharpKernel5X5,borderType=cv2.BORDER_CONSTANT)
sharp2 = cv2.filter2D(img3,-1,sharpKernel5X5,borderType=cv2.BORDER_CONSTANT)

media = cv2.filter2D(img,-1,sharpKernel5X5,borderType=cv2.BORDER_CONSTANT)
media2 = cv2.filter2D(img2,-1,sharpKernel5X5,borderType=cv2.BORDER_CONSTANT)

cv2.imwrite('sharp5x5.jpg', sharp)
cv2.imwrite('sharpBYELO5x5.jpg', sharp2)
cv2.imwrite('media5x5.jpg',media)
cv2.imwrite('mediaBYELO5x5.jpg',media2)


