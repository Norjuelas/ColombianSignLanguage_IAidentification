import numpy as np
import matplotlib.pyplot as plt


img=100*np.ones((10,10,3))


#Todos los valores de ancho por alto de la matriz (Tal color)
R=img[:,:,0]
G=img[:,:,1]
B=img[:,:,2]



#Todos los valores de esta matriz
R[:,:]=255
G[:,:]=255
B[:,:]=0

print(img)

plt.imshow(img)
plt.show()