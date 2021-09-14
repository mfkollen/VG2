import random



terning = 0

stopp = 0

while True:
    input("Trykk for tilfeldig tall")
    terning = random.randint(1,999)
    print (terning)
    if terning == 571:
        break
        
    

terning = 0


while True:
    valg = input("Trykk for tilfeldig tall")
    terning = random.randint(1,999)
    print (terning)
    if valg == "stopp":
        break

    