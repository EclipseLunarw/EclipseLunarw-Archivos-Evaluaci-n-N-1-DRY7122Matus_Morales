#Pregunta 4
#Crear un script en Python que el usuario pueda ingresar por teclado datos de un equipo de red. 
a = 0
while a < 1:
    equipo = {}

    equipo["Datacenter"] = input("Ingrese el nombre del datacenter : ")
    equipo["Tipo_de_equipo"] = input("ingrese el nombre del equipo : ")
    equipo["modelo_equipo"] = input("Ingrese el tipo de equipo : ")
    equipo["sala"] = input("Ingrese la sala : ")
    equipo["rack"] = input("Ingrese el rack : ")
    equipo["num_u_rack"] = int(input("Ingrese el número de U de rack : "))
    equipo["ip_principal"] = input("Ingrese la IP principal : ")

    interface = {}
    num_interface = int(input("Ingrese la cantidad de interfaces que posee : "))
    for _ in range(num_interface):
        tipo_interface = input("Ingrese el tipo de interface : ")
        cantidad = int(input(f"Ingrese la cantidad de interface {tipo_interface} : "))
        interface[tipo_interface] = cantidad

    equipo["interfaces"] = interface


    print("Datos del equipo de red:")
    for key, value in equipo.items():
        if key == "interface":
            print("Interface :")
            for tipo, cantidad in value.items():
                print(f"- {cantidad} interfaces {tipo}")
        else:
            print(f"{key.capitalize()}: {value}")
    b = int(input("Desea agregar otros datos? 1 - si 0 - no :"))
    if b == 0:
        a=1