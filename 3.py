#Pregunta 3
#Crear un script en Python que al momento que un usuario introduzca el número de ACL IPv4, señale si es una ACL Estándar, Extendida o el número no corresponde a una lista de acceso.
def acl(numero_acl):
    if 1 <= int(numero_acl) <= 99:
        return "ACL Estandar"
    elif 100 <= int(numero_acl) <= 199:
        return "ACL Extendida"
    else:
        return "El numero no corresponde a una ACL"
    
numero_acl = input("Ingrese el numero de ACL IPv4 que desea ver: ")

verificador = acl(numero_acl)
print(f"El numero {numero_acl} es {verificador}")