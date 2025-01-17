"100KMh" "tank muss man eingeben" "gefahrene KM muss man eingeben"


try:
    kraftstoff = float(input("Bitte gib die gesamte Menge an Kraftstoff ein: "))
    km = float(input("Bitte gib die gefahrenen KM ein: "))
    eurPer100km = float(input("Bitte gib ein, wieviel du für den Sprit pro 100km bezahlt hast: "))
    usagePer100km = (kraftstoff / km) * 100
        ##usagePer100km = (kraftstoff / km) * 100
    preisPro100km = usagePer100km * eurPer100km
    print(f"Dein Durchschnittsverbrauch liegt bei: {usagePer100km: .2f} Liter/100KM")
    print(f"Du hast pro 100km{preisPro100km: .2f}€ gezahlt")
except ValueError:
    print("Was soll das??")
