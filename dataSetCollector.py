import os
import cv2

os.makedirs("customModel/dataSet/train/bottle", exist_ok = True)
os.makedirs("customModel/dataSet/train/cookie", exist_ok = True)

# os.makedirs("customModel/train/fondo", exist_ok = True)

cap = cv2.VideoCapture(0)
carpeta = "bottle"
lineaMemoriaActual = 0
countBottle = 0
countCookie = 0

# En el archivo memoria la primera linea es la cuenta de bottle y la segunda cookie
# Leer memoria y recordar cuenta para cada 
with open("memoria.txt", "r") as memoria:
    cuentas = memoria.readlines()
    countBottle = cuentas[0]
    countCookie = cuentas[1]



while True:
    ret, frame = cap.read()
    
    cv2.imshow("Dataset", frame)


    key = cv2.waitKey(1)

    #if key == ord("e"):
    #    carpeta = "fondo"
    #    numero = 0
    if key == ord("a"):
        carpeta = "bottle"
        numero = countBottle
        lineaMemoriaActual = 0
    if key == ord("s"):
        carpeta = "cookie"
        numero = countCookie
        lineaMemoriaActual = 1
    elif key == ord(" "):
        cv2.imwrite(f"customModel/dataSet/train/{carpeta}/{numero}.jpg", frame)
        numero = numero + 1
        
            
    elif key == ord("q"):

        break

#cap.release()
#cv2.destroyAllWindows()
