høyde = 0
bredde = 0

#areal og omkrets av en firkant
høyde = int(input("Skriv inn høyden"))
bredde = int(input("Skriv inn bredden "))


areal = 0
omkrets = 0

areal = bredde * høyde
print("arealet til objektet er:" + str(areal))

omkrets = 2*bredde + 2*høyde
print("Omkretsen er:" + str(omkrets))

