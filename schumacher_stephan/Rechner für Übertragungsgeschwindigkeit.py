print("Rechner für Übertragungsgeschwindigkeit")
print("Eingabe in GB oder MB? Bitte angeben. \n")
z=(input("GB" or "MB"))
if z == "GB":
        print("Bitte Werte eingeben \n")
        d = float(input("1. Wert in GB "))
        c = float(input("2. Wert in MBit/s "))
        T = ((d*8*1000) / c)
        GT = T/60
        if T < 60:
            print("Die Übertragung dauert: {0:5f} Sekunden".format(T))
        else:
            print("Die Übertragung dauert: {0:5f} Minuten".format(GT))
elif z == "MB":
        print("Bitte Werte eingeben \n")
        d = float(input("1. Wert in MB "))
        c = float(input("2. Wert in MBit/s "))
        T = ((d*8) / c)
        GT = T/60
        if T < 60:
            print("Die Übertragung dauert: {0:5f} Sekunden".format(T))
        else:
            print("Die Übertragung dauert: {0:5f} Minuten".format(GT))
else: print("ANGABE NUR ""MB"" ODER ""GB""")


