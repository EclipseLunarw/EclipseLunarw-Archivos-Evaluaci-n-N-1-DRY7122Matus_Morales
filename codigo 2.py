#Pregunta 2
#Crear un script en Python que solicite información como el nombre, apellido, Código-sección y sede. La información debe aparecer en pantalla.
a = 0
while a < 1 :
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    seccion = input("Ingrese su numero de sección: ")
    sede = input("Ingrese su sede: ")

    print("Información ingresada")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Código de sección:", seccion)
    print("Sede:", sede)
    b = int(input("Desea ingresar otros datos? 1- Si 0- No :"))
    if b == 0:
        a=1