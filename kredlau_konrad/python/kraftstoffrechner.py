def kraftstoff_verbrauch_und_kosten():
    gefahrene_kilometer = float(input("Geben Sie die gefahrenen Kilometer ein: "))
    getankte_liter = float(input("Geben Sie die getankte Menge an Kraftstoff (in Litern) ein: "))
    literpreis = float(input("Geben Sie den Literpreis für den Kraftstoff ein: "))

    durchschnittsverbrauch = (getankte_liter / gefahrene_kilometer) * 100

    kosten = durchschnittsverbrauch * literpreis

    print(f"Durchschnittsverbrauch: {durchschnittsverbrauch:.2f} Liter/100 km")
    print(f"Gesamtkosten: {kosten:.2f} Euro")


kraftstoff_verbrauch_und_kosten()
