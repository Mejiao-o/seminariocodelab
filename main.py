# importar funciones
from titulo1 import titulo #Listo
from problema2 import problema #Listo
from justificacion3 import justificacion #Listo
from objetivo4 import objetivo #Listo
from marcoTeorico5 import marco #Listo
from metodologia6 import metodologia
from reconocerResiduos7 import programa
from conclusiones8 import conclusiones
from referencias9 import referencias
from desarrollador10 import desarrollador

#Menu
while True:
    print("<<<Menu>>>")
    print("1. Titulo")
    print("2. Problema a solucionar")
    print("3. ¿Por que se hace el proyecto?")
    print("4. Objetivo")
    print("5. Marco Teorico")
    print("6. Metodologia")
    print("7. Reconocer residuos solidos")
    print("8. Conclusiones")
    print("9. Referencias")
    print("10. Desarrollador")
    print("11. Cerrar")
 
    Eleccion = int(input("Ingresa un numero del Menu: "))

    if Eleccion == 1:
        titulo()
    if Eleccion == 2:
        problema()
    if Eleccion == 3:
        justificacion()
    if Eleccion == 4:
        objetivo()
    if Eleccion == 5:
        marco()
    if Eleccion == 6:
        metodologia()
    if Eleccion == 7:
        programa()
    if Eleccion == 8:
        conclusiones()
    if Eleccion == 9:
        referencias()
    if Eleccion == 10:
        desarrollador()
    if Eleccion == 11:
        print("Adios!")
        break