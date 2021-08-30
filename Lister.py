from typing import OrderedDict

def telle():
    for i in range(70):
        print(i)
    if i == 35:
        print("Du er halvveis")

def frukt():
    frukt = ["Eple","Pære","Sitron","Melon"]

    frukt.append("Plomme")

    nfrukt = input("Skriv inn en frukt")
    frukt.append(nfrukt)

    print(frukt)


klasse = []
elev = 0

while True: 
    elev = input("Skriv inn et navn: ")

    if elev =="stopp":
        break

    klasse.append(elev)
    print(klasse)



