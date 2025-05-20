continuar=True
total=0
fulls=0
standards=0
basicos=0
chinchinfulls=0
chinchinstandards=0
chinchinbasicos=0
chinchin=0


def pagolavado():
    print ('''que tipo de lavado decea?
           - full:      $ 15000
           - standard   $ 10000
           - basico     $ 7000''')
    opcion=int(input())
    match opcion:
        case 1:
            total+=1
            fulls+=1
            chinchinfulls+=15000
            chinchin+=15000
        case 2:
            total+=1
            standards+=1
            chinchinstandards+=10000
            chinchin+=10000
        case 3:
            total+=1
            basicos+=1
            chinchinbasicos+=7000
            chinchin+=7000


def cuentasdiarias():
    print("han ingresado ",total," autos")
    print("se han recaudado $",chinchin)
    if chinchinfulls>chinchinstandards and chinchinfulls>chinchinbasicos:
        print("full, es el servicio que mas recaudo ($",chinchinfulls,")")
    elif chinchinstandards>chinchinfulls and chinchinstandards>chinchinbasicos:
        print("standard, es el servicio que mas recaudo ($",chinchinstandards,")")
    elif chinchinbasicos>chinchinfulls and chinchinbasicos>chinchinstandards:
        print("basico, es el servisio que mas recaudo ($",chinchinbasicos,")")

    detalle=input("decea el detalle? y/n")
    if detalle=="y":
        print("se realizaron ",fulls," full, recaudando $",chinchinfulls)
        print("se realizaron ",standards," standard, recaudando $",chinchinstandards)
        print("se realizaron ",basicos," full, recaudando $",chinchinbasicos)


while continuar:
    print('''seleccione una opcion:
          1- ingresar servicio
          2- ver cuentas diarias
          3- salir''')
    opci=int(input())
    match opci:
        case 1:
            pagolavado()
        case 2:
            cuentasdiarias()
        case 3:
            continuar=False
