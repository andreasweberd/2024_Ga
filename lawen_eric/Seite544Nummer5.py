gefahreneKilometer = int(input("Gefahrene Kilometer: "))
tankMenge = int(input("Getankte Menge in Liter: "))
preisProLiter = float(input("Preis pro Liter Kraftstoff in Cent: "))

def verbrauchBerechnen():
    literProKilometer = tankMenge/gefahreneKilometer

    literPro100Kilometer = literProKilometer*100

    print("Durschnittsverbrauch pro 100 Kilometer: "+str(literPro100Kilometer)+" Liter")

    return literPro100Kilometer

def kostenBerechnen(literverbrauchAuf100Kilometer):
    gesamteKosten = literverbrauchAuf100Kilometer*preisProLiter
    print("Kosten für 100 Kilometer Strecke: "+str(gesamteKosten)+" Euro")

literPro100Kilometer = verbrauchBerechnen()
kostenBerechnen(literPro100Kilometer)