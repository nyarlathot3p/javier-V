votantes=int(input("ingrese numero de voltantes "))
op1=0
op2=0
op3=0
candidato1="kaiser"
candidato2="nose"
for i in range(votantes):
    print("por quien decea votar?")
    print(candidato1,": presione 1")
    print(candidato2,": presione 2")
    print("voto en blanco: presione 0")
    voto=int(input())
    if voto==1:
        op1+=1
    elif voto==2:
        op2+=1
    elif voto==0:
        op3+=1
#suma votos blanco
if op1>op2:
    op1=op1+op3
elif op2>op1:
    op2=op2+op3
print ("los votos de ", candidato1, " son ", op1)
print ("los votos de ", candidato2, " son ", op2)
if op2>op1:
    print("el ganador es: ", candidato2)
elif op1>op2:
    print("el ganador es: ", candidato1)
else:
    print("es un empate")

    git config --global user.email "you@example.com"
>>   git config --global user.name "Your Name"