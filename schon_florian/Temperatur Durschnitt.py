def durschnittstemperatur(temperaturen):
    try:
        return(sum(temperaturen) / len(temperaturen))
    except:
        return("Es wurden keine Temperaturen angegeben")

temperaturen = []
'''
laenge = int(input("Wieviele Temperaturen werden angegeben? "))
while laenge > 0:
    try:
        eingabe = float(input("Gib eine Temperatur als float ein: "))
        temperaturen.append(eingabe)
        laenge = laenge - 1
    except:
        print("Die Eingabe war kein float, versuche es erneut")
'''

i = 0
while i == 0:
    try:
        eingabe = float(input("Gib eine Temperatur als float ein: "))
        temperaturen.append(eingabe)
    except:
        i+=1
        print("Die Eingabe wurde beendet")

print("Die Durschnittstemperatur beträgt:", durschnittstemperatur(temperaturen))