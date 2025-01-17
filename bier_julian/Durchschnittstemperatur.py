# Benutzer wird aufgefordert, die Anzahl der Temperaturwerte einzugeben
n = int(input("Wie viele Temperaturwerte möchtest du eingeben? "))

# Initialisierung des Arrays (Liste) für die Temperaturwerte
temperaturen = []

# Benutzer wird aufgefordert, n Temperaturwerte einzugeben
for i in range(n):
    temp = float(input(f"Gib Temperaturwert {i+1} ein: "))
    temperaturen.append(temp)

# Berechnung der Durchschnittstemperatur
durchschnitt = sum(temperaturen) / len(temperaturen)

# Ausgabe der Durchschnittstemperatur
print("Die Durchschnittstemperatur beträgt:", durchschnitt)
