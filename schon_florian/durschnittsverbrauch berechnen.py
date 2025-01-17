<<<<<<< HEAD
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

=======
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

>>>>>>> 98d08f914f2abde6feb35121a42bbbbce638297c
print("Der Durschnittsverbrauch auf 100km beträgt:", durschnittsverbrauch())