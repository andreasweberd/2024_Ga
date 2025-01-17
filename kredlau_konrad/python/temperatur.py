# Verwendung von float für . Zahlen
temp1 = float(input("Gib die 1. Temperatur ein: "))
temp2 = float(input("Gib die 2. Temperatur ein: "))
temp3 = float(input("Gib die 3. Temperatur ein: "))

durchschnitt = (temp1 + temp2 + temp3) / 3

print(f"Die Durchschnittstemperatur beträgt: {durchschnitt:.2f} Grad")
