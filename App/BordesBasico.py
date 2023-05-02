import cv2
from matplotlib import pyplot as plt
import numpy as np

# Conectar a camara 
cap = cv2.VideoCapture(0)

# ciclo que genera marcos de la camara

while cap.isOpened(): 
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(frame, (3,3),0)
    canny = cv2.Canny(blurred, threshold1=180, threshold2=200)
    cv2.imshow("Webcam", canny)



cv2.destroyAllWindows()