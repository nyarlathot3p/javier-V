lista_productos=[]
#menu
while True:
    print('''seleccione una opcion
        1- agregar un producto
        2- quitar un producto
        3- mostrar todos los productos
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
            abregar=input("ingrese el producto que decea agregar:  ")
            lista_productos.append(abregar)
        case 2:
            quitar=input("ingrese el producto que decea quitar:  ")
            lista_productos.append(quitar)
        case 3:
            for i in lista_productos:
                place=1
                print(place,"- ",i)
                place+=1
        case 4:
            print("adios")
            break
        case _:
            print("ERROR favor ingresar una opcion valida")