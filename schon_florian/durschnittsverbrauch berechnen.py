def durschnittsverbrauch():
    try:
        gefahreneKilometer = float(input("Gib die gefahrenen Kilometer an "))
    except:
        print("Die Eingabe war ungültig")
    try:
        getankteMenge = float(input("Gib die getankte Menge an "))
    except:
        print("Die Eingabe war ungültig")
    try:
        return(getankteMenge/ gefahreneKilometer * 100)
    except:
        return("Bei der Berechnung ist ein Fehler aufgetreten")

print("Der Durschnittsverbrauch auf 100km beträgt:", durschnittsverbrauch())