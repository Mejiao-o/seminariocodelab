import os
import cv2

def mostrarEstado():
    print("La carpeta actual es: ", precarpeta)
    print("La subcarpeta actual es: ", carpeta)

os.makedirs("customModel/dataSet/train/bottle", exist_ok = True)
os.makedirs("customModel/dataSet/train/paper", exist_ok = True)
os.makedirs("customModel/dataSet/train/cookie", exist_ok = True)
os.makedirs("customModel/dataSet/test/bottle", exist_ok = True)
os.makedirs("customModel/dataSet/test/paper", exist_ok = True)
os.makedirs("customModel/dataSet/test/cookie", exist_ok = True)

cap = cv2.VideoCapture(0)
precarpeta = "train"
carpeta = "bottle"

# En el archivo memoria la primera linea es la cuenta de bottle y la segunda paper
# Leer memoria y recordar cuenta para cada 
with open("memoria.txt", "r") as memoria:
    cuentas = memoria.readlines()
    StrBottle = cuentas[0]
    StrPaper = cuentas[1]
    StrCookie = cuentas[2]
    StrTestBottle = cuentas[3]
    StrTestPaper = cuentas[4]
    StrTestCookie = cuentas[5]


countBottle = int(StrBottle)
countPaper = int(StrPaper)
countCookie = int(StrCookie)
countTestBottle = int(StrTestBottle)
countTestPaper = int(StrTestPaper)
countTestCookie = int(StrTestCookie)

while True:
    ret, frame = cap.read()
    
    cv2.imshow("Dataset", frame)

    key = cv2.waitKey(1)

    if key == ord("a"):
        carpeta = "bottle"
        mostrarEstado()
    if key == ord("s"):
        carpeta = "paper"
        mostrarEstado()
    if key == ord("d"):
        carpeta = "cookie"
        mostrarEstado()
    if key == ord("r"):
        precarpeta = "train"
        mostrarEstado()    
    if key == ord("t"):
        precarpeta = "test"
        mostrarEstado()
    elif key == ord(" "):
        if precarpeta == "train":
            if carpeta == "bottle":
                cv2.imwrite(f"customModel/dataSet/train/{carpeta}/{countBottle}.jpg", frame)
                countBottle = countBottle + 1
            elif carpeta == "paper":
                cv2.imwrite(f"customModel/dataSet/train/{carpeta}/{countPaper}.jpg", frame)
                countPaper = countPaper + 1
            elif carpeta == "cookie":
                cv2.imwrite(f"customModel/dataSet/train/{carpeta}/{countCookie}.jpg", frame)
                countCookie = countCookie + 1
        if precarpeta == "test":
            if carpeta == "bottle":
                cv2.imwrite(f"customModel/dataSet/test/{carpeta}/{countTestBottle}.jpg", frame)
                countTestBottle = countTestBottle + 1
            elif carpeta == "paper":
                cv2.imwrite(f"customModel/dataSet/test/{carpeta}/{countTestPaper}.jpg", frame)
                countTestPaper = countTestPaper + 1
            elif carpeta == "cookie":
                cv2.imwrite(f"customModel/dataSet/test/{carpeta}/{countTestCookie}.jpg", frame)
                countTestCookie = countTestCookie + 1

    elif key == ord("q"):
        with open("memoria.txt", "w") as memoria:
            memoria.write(f"{countBottle}\n")
            memoria.write(f"{countPaper}\n")
            memoria.write(f"{countCookie}\n")
            memoria.write(f"{countTestBottle}\n")
            memoria.write(f"{countTestPaper}\n")
            memoria.write(f"{countTestCookie}\n")
        break

cap.release()
cv2.destroyAllWindows()
