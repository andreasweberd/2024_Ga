
def avg(temperaturen):
     return sum(temperaturen) / len(temperaturen)
n = int(input("Wie viele Temperaturwerte möchtest du eingeben? "))
temperaturen = []
for i in range(n):
     temp = float(input(f"Gib Temperaturwert {i+1} ein: "))
     temperaturen.append(temp)
durchschnitt = avg(temperaturen)
print(f"Die Durchschnittstemperatur beträgt: {durchschnitt:.2f}")
