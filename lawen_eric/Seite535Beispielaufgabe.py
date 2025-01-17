try:    
    #inputcount = int(input("Anzahl der Eingaben: "))

    inputarray = []

    def eingabe():
        x = 1
        while True:
            inputarray.append(float(input("Temperaturwert "+str(x)+": ")))
            x += 1

    def average(array):
        return sum(array)/len(array)

    eingabe()

    print("Durschnittstemperatur: "+str(average(inputarray)))
except:
    print("Fehlerhafte Eingabe! Eingabe ist keine gültige Zahl!")
finally:
    print("Durschnittstemperatur: "+str(average(inputarray)))