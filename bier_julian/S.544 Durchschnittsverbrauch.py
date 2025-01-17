def avg(verbrauch):
    return (verbrauch[1] / verbrauch[0]) * 100

try:
    gefahrene_kilometer = float(input("Gib die gefahrenen Kilometer ein: "))
    getankter_kraftstoff = float(input("Gib die getankte Menge an Kraftstoff (in Litern) ein: "))
    literpreis = float(input("Gib den Literpreis für den Kraftstoff ein: "))

    verbrauch = avg((gefahrene_kilometer, getankter_kraftstoff))
    kosten = (getankter_kraftstoff * literpreis)  # Korrigierte Kostenberechnung

    print(f"Der durchschnittliche Kraftstoffverbrauch beträgt: {verbrauch:.2f} Liter pro 100 km")
    print(f"Gesamtkosten: {kosten:.2f} Euro")

except ValueError:
    print("Bitte geben Sie gültige Zahlen ein.")
except ZeroDivisionError:
    print("Die gefahrenen Kilometer dürfen nicht null sein.")
finally:
    print("Berechnung abgeschlossen.")
