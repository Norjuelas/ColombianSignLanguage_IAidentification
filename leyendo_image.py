import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread("C:/Users/Jeison Diaz/OneDrive/Documentos/GitHub/SignalS/ColombianSignLanguage_IAidentification/girasol.jpg")


#Informacion de la imagen
toma=img.shape

#Tipo de los datos de cada pixel
tipo=img.dtype

#Si imprimimos la imagen podremos ver que tiene en cada pixel
print(img)


#print(toma,tipo)

cv2.imshow("IMG",img)

plt.imshow(img)
plt.show()
