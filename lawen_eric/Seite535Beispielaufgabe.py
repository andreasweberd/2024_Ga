try:    
    inputcount = int(input("Anzahl der Eingaben: "))

    inputarray = []

    def eingabe():
        for x in range(inputcount):
            inputarray.append(float(input("Temperaturwert "+str(x+1)+": ")))

    def average(array):
        return sum(array)/len(array)

    eingabe()

    print("Durschnittstemperatur: "+str(average(inputarray)))
except:
    print("Fehlerhafte Eingabe!")
finally:
    print("Alle vorherigen Werte:")
    for singleinput in inputarray:
        print(singleinput)