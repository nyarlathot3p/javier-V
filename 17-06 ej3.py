lista_productos=[{"nombre":"lapiz","precio":400},{"nombre":"goma","precio":300},{"nombre":"estuche","precio":1600}]

while True:
    print('''seleccione una opcion
        1- agregar un articulo
        2- borrar ariculo
        3- Actualizar Articulo
        4- mostrar listado de articulos
        5- salir
        ''')
    while True:
        try:
            opcion=int(input())
            if opcion <1 or opcion>5:
                print("ERROR opcion no valida")
            else:
                break
        except Exception:
            print("ERROR opcion invalida")
    match(opcion):
        case 1:
            nuevo_producto=input("indique el articulo que decea agregar:  ")
            nuevo_precio=int(input("indique el articulo que decea agregar:  "))
            lista_productos.append({"nombre":nuevo_producto,"precio":nuevo_precio})
        case 2:
            quitar=input("indique el articulo que decea quitar:  ")
            n=0
            for item in lista_productos:
                if item["nombre"]==quitar:
                    lista_productos.pop(n)
                n+=1
        case 3:
            cambiar=input("indique el articulo que decea actualizar:  ")
            n=0
            for elemento in lista_productos:
                if elemento["nombre"]==cambiar:
                    cambio_nombre=input("desea cambiar el nombre si/no: ")
                    while cambio_nombre!="si" and cambio_nombre!="no":
                        print("ERROR  limite su respuesta a 'si' o 'no'")
                        cambio_nombre=input("desea cambiar el nombre si/no: ")
                    if cambio_nombre=="si":
                        nombre_actualizado=input("ingrese el nuevo nombre del producto")
                        elemento["nombre"]=nombre_actualizado
                    cambio_precio=input("desea cambiar el precio si/no: ")
                    while cambio_precio!="si" and cambio_precio!="no":
                        print("ERROR  limite su respuesta a 'si' o 'no'")
                        cambio_precio=input("desea cambiar el pecio si/no: ")
                    if cambio_precio=="si":
                        precio_actualizado=input("ingrese el nuevo precio del producto")
                        elemento["precio"]=precio_actualizado                     
                    n+=1
            if n==0:
                print("el articulo que indico no existe")
        case 4:
            printable="producto                                valor"
            print(printable)
            for item in lista_productos:
                print(item["nombre"],(len(printable)-2-len(item["nombre"]+str(item["precio"])))*" ",item["precio"])
        case 5:
            print("adios")
            break
        case _:
            print("ERROR favor ingresar una opcion valida")