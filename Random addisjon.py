import random


def terningkast():
    terning1 = 0
    terning2 = 0
    sum = 0

    while sum!= 12:
        input("Trykk for å kaste terning")
        terning1 = random.randint(1,6)
        terning2 = random.randint(1,6)
        sum = terning1 + terning2
        print(" \n Du fikk", sum)


terningkast()










