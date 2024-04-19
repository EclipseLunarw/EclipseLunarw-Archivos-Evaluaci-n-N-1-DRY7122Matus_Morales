#Pregunta 4
#Crear un script en Python que el usuario pueda ingresar por teclado datos de un equipo de red. 

def ingresar_equipo():
    equipo = {}
    print("Bienvenido al Diccionario de equipos de Red")
    equipo["Datacenter"] = input("\nIngrese el nombre del datacenter : ")
    equipo["Tipo_de_equipo"] = input("ingrese el nombre del equipo : ")
    equipo["modelo_equipo"] = input("Ingrese el modelo del equipo : ")
    equipo["sala"] = input("Ingrese la Sala : ")
    equipo["rack"] = input("Ingrese el Rack : ")
    equipo["num_u_rack"] = input("Ingrese el número de U de rack : ")
    equipo["ip_principal"] = input("Ingrese la IP principal : ")
    equipo["Interfaces"] = {}
    num_interface = int(input("Ingrese la cantidad de interfaces que posee : "))
    for i in range(num_interface):
        tipo = input(f"Tipo de la interfaz {i+1}: ")
        cantidad = int(input(f"Cantidad de interfaces de tipo {tipo}: "))
        equipo["Interfaces"][tipo] = cantidad
    return equipo

def buscar_equipo(equipos, nombre):
    if nombre in equipos:
        print("Datos del equipo:")
        for key, value in equipos[nombre].items():
            print(f"{key}: {value}")
    else:
        print("El equipo no fue encontrado.")


def main():
    equipos = {}
    while True:
        opcion = input("1. Ingresar equipo\n2. Buscar equipo por nombre\n3. Salir\nIngrese su opción: ")
        if opcion == "1":
            equipo = ingresar_equipo()
            equipos[equipo["tipo_de_equipo"]] = equipo
            print("Equipo ingresado correctamente.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del equipo a buscar: ")
            buscar_equipo(equipos, nombre)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
if __name__ == "__main__":
    main()