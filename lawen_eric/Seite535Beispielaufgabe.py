inputcount = int(input("Anzahl der Eingaben: "))

array = []

def eingabe():
    for x in range(inputcount):
        array.append(float(input("Temperaturwert "+str(x+1)+": ")))

def average(x):
    return sum(x)/len(x)

eingabe()

print("Durschnittstemperatur: "+str(average(array)))