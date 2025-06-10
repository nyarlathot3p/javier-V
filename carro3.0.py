carro=["a","b","c"]
precios=[1,2,3]

#ingresar producttos
def opcion1():
    nuevo_item=input("ingrese el nombre del nuevo producto")
    carro.append(nuevo_item)
    costo_nuevo_item=("ingrese presio del producto")
    precios.append(costo_nuevo_item)

#comprar (submenu)
def opcion2():
    print("?")

#crear boleta
def opcion3():
    total=0
    locate=0
    for item in carro:
        total+=precios[locate]
        espacio=" "*(20-(len(carro[locate])+len(str(precios[locate]))))
        print(carro[locate],espacio,precios[locate])
        locate+=1
    print("total      ",total)




while True:
    print('''seleccione una opcion
        1- ingresar producto
        2- comprar (submenu)
        3- crear boleta
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
            opcion1()
        case 2:
            opcion2()
        case 3:
            opcion3()
        case 4:
            print("adios")
            break
        case _:
            print("ERROR favor ingresar una opcion valida")