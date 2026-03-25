import cv2
from colorama import Fore, Back


def marco():
    print("")
    print(F"{Fore.CYAN}5. Marco Teorico")
    print(Fore.RESET)
    print(f"{Fore.RED}Este es el marco teorico que nos ayudo a desarrollar este proyecto")
    print(f"{Fore.BLUE}Cierre la pestaña que aparece para pasar al siguiente punto")
    print(Fore.RESET)

    imgVisionArtificial = cv2.imread("vision-artificial.jpeg")

    cv2.putText(
        imgVisionArtificial,
        "La vision artificial es un subcampo de la IA",
        (310,275),
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        0.7,
        (0,0,0),
        lineType=cv2.QT_FONT_BOLD,
        thickness=1)
    
    cv2.putText(
        imgVisionArtificial,
        "que usa algoritmos para darle la capacidad",
        (315,295),
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        0.7,
        (0,0,0),
        lineType=cv2.QT_FONT_BOLD,
        thickness=1)
    
    cv2.putText(
        imgVisionArtificial,
        "a una maquina de analizar imagenes y extraer",
        (302,315),
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        0.7,
        (0,0,0),
        lineType=cv2.QT_FONT_BOLD,
        thickness=1)
    
    cv2.putText(
        imgVisionArtificial,
        "informacion para posteriormente ser analizada",
        (302,335),
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        0.7,
        (0,0,0),
        lineType=cv2.QT_FONT_BOLD,
        thickness=1)
    
    cv2.imshow("¿Que es la vision artifical?", imgVisionArtificial)
    cv2.waitKey(0)



    imgOpenCv = cv2.imread("1_HfZmZayUqnYioPC9qTfd4A.webp")
    
    cv2.putText(
        imgOpenCv,
        "OpenCv es una libreria de python encargada de",
        (310,455),
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        0.7,
        (0,0,0),
        lineType=cv2.QT_FONT_BOLD,
        thickness=1)
    cv2.putText(
        imgOpenCv,
        "facilitar el desarrollo de vision artifial y procesamiento de imagenes",
        (250,485),
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        0.7,
        (0,0,0),
        lineType=cv2.QT_FONT_BOLD,
        thickness=1)
    
    cv2.imshow("¿Que hace la libreria OpenCV?", imgOpenCv)
    cv2.waitKey(0)

    print(f"{Fore.WHITE} UNA FORMA DE DETECCION DE VISION ARTIFICIAL: {Fore.BLUE} E{Fore.RED}L{Fore.GREEN} C{Fore.MAGENTA}O{Fore.YELLOW}L{Fore.WHITE}O{Fore.CYAN}R")
    print("")
    print(f"{Fore.LIGHTMAGENTA_EX} esta tiene 4 fases:")
    print(f"{Fore.CYAN} 1. Suavizado")
    print(f"{Fore.WHITE}     Consiste en aplicar un filtro gauseano (el cual consiste en promediar el color de los pixeles con respecto a los cercanos) a la imagen que se desea analiazar para asi eliminar parte de el reuido que se pueda producir en la imagen")
    print("")
    print(f"{Fore.CYAN} 2. Conversion a HSV")
    print(f"{Fore.WHITE}     Convierte la escala de color que usa la camara por defecto (GBR) a una escala que facilita la seleccion de colores mas especificos ya que separa el color de la saturacion y el valor")
    print("")
    print(f"{Fore.CYAN} 3. Mascara Binaria")
    print(f"{Fore.WHITE}     Examina si el color de un determinado pixel entra dentro del rango determinado y asigna correspondientemente blanco si esta dentro del rango o negro si no lo esta")
    print("")
    print(f"{Fore.CYAN} 4. Detectar y dibujar bordes")
    print(f"{Fore.WHITE}     Crea un borde al rededor del area seleccionada y se dibuja un rectangulo con el nombre del color identificado")
    print("")