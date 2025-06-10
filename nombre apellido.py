nombres=["1","2","3","4","5","6","7","8"]
apellidos=["a","b","c","a","e","f","g","h"]



def agregar_n(a,b):
    nombre=float(input("ingrese nombre"))
    a.append(nombre)
    nombre=float(input("ingrese apellido"))
    b.append(nombre)

def mostrar(a,b):
    for n in range(len(nombres)):
        print(a[n]," ",b[n])

def buscar_nombre(a,b):
    buscado=input("que nombre desea buscar? ")
    n=-1
    cons=0
    coincidencias=[]
    for i in range(len(a)):
        print(i)
        print(a[i])
        if a[i]==buscado:
            print("--")
        

while True:
    print('''seleccione una opcion
        1- insertar nombre y apellido
        2- mostrar nombres y apellidos
        3- buscar nombre
        4- salir
        ''')
    while True:
        try:
            opcion=int(input())
            if opcion <1 or opcion>4:
                print("ERROR opcion no valida")
            else:
                break
        except Exception:
            print("ERROR opcion invalida")

    match(opcion):
        case 1:
            agregar_n(nombres,apellidos)
        case 2:
            mostrar(nombres,apellidos)
        case 3:
            buscar_nombre(nombres,apellidos)
        case 4:
            print("adios")
            break
        case _:
            print("ERROR favor ingresar una opcion valida")