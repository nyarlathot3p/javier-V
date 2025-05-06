
ingreso=float(input("de cuanto es su ingreso"))
print("cual es su nivel educacional")
print("1- basico        2- medio        3- superior")
nivel=int(input(""))
nacionalidad=input("cual es su nacionalodad?")


if ingreso>500000 and ingeso<=1000000:
    In=300000
elif ingreso>1000000 and ingeso<=1500000:
    In=650000
elif ingreso>1500000:
    In=300000

if nivel==1:
    mult=1
elif nivel==2:
    mult=1.3
elif nivel==3:
    mult=1.5

if nacionalidad=="chilena" or nacionalidad=="chileno":
    bono=30000
else:
    bono=0

print("su puntaje de credito es: ",In*mult+bono)