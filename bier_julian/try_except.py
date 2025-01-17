def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")

while True:
    try:
        n = int(input("Wie viele Temperaturwerte möchtest du eingeben? "))
        if n <= 0:
            raise ValueError("Die Anzahl der Temperaturwerte muss größer als 0 sein.")
        break
    except ValueError as e:
        print(e)
temperaturen = []

for i in range(n):
    temp = get_float_input(f"Gib Temperaturwert {i+1} ein: ")
    temperaturen.append(temp)

durchschnitt = sum(temperaturen) / len(temperaturen)

print("Die Durchschnittstemperatur beträgt:", durchschnitt)
