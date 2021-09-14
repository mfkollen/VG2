Tall1 = 0
Tall2 = 0
sum = 0
valg = 0



        

def addere():
    Tall1 = int(input("Gi meg et tall"))
    Tall2 = int(input("Gi meg et tall til"))

  
    sum = int(Tall1) + int(Tall2)
    print("Summen av tall 1 og tall 2 er:" + str (sum))




def multiplisere():
    Tall1 = int(input("Gi meg et tall"))
    Tall2 = int(input("Gi meg et tall til"))

    sum = int(Tall1) * int(Tall2)
    print("\n Produktet av tall 1 og tall 2 er:" + str (sum))



valg = int(input(" Skriv 1 for addisjon og 2 for multiplikasjon"))

if valg == 1:
    addere()
elif valg == 2:
    multiplisere()
else:
    print(" \n Det du skrev er ikke gyldig \n")
