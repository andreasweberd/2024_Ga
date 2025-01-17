def avgSpritverbrauch(gefahreneKilometer, getankterKraftstoff):
    verbrauch = getankterKraftstoff/gefahreneKilometer*100
    print(f'Der durchschnittliche Kraftstoffverbrauch pro 100 Kilometer beträgt {verbrauch:.2f} Liter')
    return verbrauch

def kraftstoffkosten(kraftstoffverbrauch, kraftstoffpreis):
    print(f'Die Kraftstoffkosten pro 100 Kilometer betragen {kraftstoffverbrauch*kraftstoffpreis:.2f}€')

gefahreneKilometer = float(input("Gefahrene Kilometer: "))
getankterKraftstoff = float(input("Getankter Kraftstoff: "))
kraftstoffpreis = float(input("Kraftstoffpreis: "))

kraftstoffverbrauch = avgSpritverbrauch(gefahreneKilometer, getankterKraftstoff)
kraftstoffkosten(kraftstoffverbrauch, kraftstoffpreis)