

def større():

    tall1 = 14
    tall2 = 7
    tall3 = 11

    if tall1 > tall2:
        print ("tall 1 er større enn tall 2")



    if (tall1 >= tall2) and (tall1 >= tall3):
        største = tall1
    elif (tall2 >= tall1) and (tall2 >= tall3):
        største = tall2
    else:
        største = tall3
        
    print ("det største tallet er:", største)


def lengst_navn():
    navn1 = "Jonathan"
    navn2 = "Tobias"
    
    print("Navnet til Jonathan har",(len(navn1)), "bokstaver")
    print("Navnet til Tobias har",(len(navn2)), "bokstaver")


    if len(navn1) > len(navn2):
        print("Navnet til Jonathan er lengst")

    if len(navn2) > len(navn1):
        print("Navnet til Tobias er lengst")



frukt = "agurk"
gronnsak = "eple"



gronnsak=gronnsak.replace("eple","agurk")
frukt=frukt.replace("agurk","eple")
print (frukt)
print (gronnsak)








        