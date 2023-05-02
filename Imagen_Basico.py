import numpy as np
import matplotlib.pyplot as plt

#Imagen Negra
                     #Ese 1 significa un solo canal una sola matriz
img=np.zeros((10,10,1))


img[0][1]=30
img[2][4]=50
img[3][1]=255
img[5][2]=230
img[6][0]=100
img[0][2]=122


plt.imshow(img,cmap='gray')

plt.show()

#Para imagenes con RGB tendremos 3 matrices superpuestas que esta compuesta
#por los colores primarios RED,BLUE,GREEN
