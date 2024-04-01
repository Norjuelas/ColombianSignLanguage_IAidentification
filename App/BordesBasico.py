import cv2

# Función para ajustar el valor de umbral
def adjust_threshold(value):
    global threshold
    threshold = value

# Conectar a la cámara 
cap = cv2.VideoCapture(0)

# Valor de umbral inicial
threshold = 180

# Crear una ventana para ajustar el valor de umbral
cv2.namedWindow('Threshold Adjustment')
cv2.createTrackbar('Threshold', 'Threshold Adjustment', threshold, 255, adjust_threshold)

# Ciclo que genera marcos de la cámara
while cap.isOpened(): 
    ret, frame = cap.read()
    if not ret:
        break
    
    # Procesamiento de la imagen
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    canny = cv2.Canny(blurred, threshold, threshold * 2)
    
    # Mostrar la imagen original en una ventana
    cv2.imshow("Original", frame)
    
    # Mostrar la imagen procesada en otra ventana
    cv2.imshow("Processed", canny)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# Liberar recursos y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
