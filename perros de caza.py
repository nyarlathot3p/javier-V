check1=False
check2=False
import random
while check1==False:
    try:
        nperros=int(input("cuantos perros de caza son: "))
    except ValueError:
        check1=False
    else:
        check1=True

while check2==False:
    try:
        cuota=int(input("cual es la cuota minima de conejos? "))
    except ValueError:
        check2=False
    else:
        check2=True

outsi=""
outno=""
for i in range(nperros):
    conejos=random.randint(0,6)
    n=str(i+1)
    if cuota<=conejos:
        print("el perro ",i+1," trajo ",cuota," conejos, por lo que tiene filete")
        outsi+= n+", "
    else:
        print("el perro ",i+1," trajo ",cuota," conejos, por lo que no tiene filete")
        outno+= n+", "
print ("los perros", outsi, "si cumplieron con la cuota")
print ("los perros", outno, "no cumplieron con la cuota")