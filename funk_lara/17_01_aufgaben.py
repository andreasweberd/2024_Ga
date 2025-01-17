n = int(input("wie viele Werte?"))

temperaturen = []

def avg (temperaturen):
    return sum(temperaturen) / len(temperaturen)

for i in range(n):
    temp = float(input("Gib Temperatur ein"))
    temperaturen.append(temp)

print(avg(temperaturen))









try: 
    print(temperaturen)
except:
    print("Fehler")
finally:
    print("Ende")

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

print(durchschnitt)







running_number = int(input("Laufende Nummer: "))
name = str(input("Name MA: "))
age = int(input("Alter MA: "))
adress = str(input("Adresse MA: "))
phone = float(input("Telefon MA: "))
job = str(input("Beruf MA: "))
married_tax = str(input("Verheiratet/Lohnst.kl. MA: "))
children = int(input("Anzahl Kinder MA: "))
salary = int(input("Lohn/Gehalt MA: "))








kilometer = float(input("Gefahrene Kilometer: "))
kraftstoff = float(input("Getankte Menge an Kraftstoff (in Litern): "))
literpreis = float(input("Preis pro Liter: "))

verbrauch_pro_100km = (kraftstoff / kilometer) * 100
kosten = verbrauch_pro_100km * literpreis

print(f"Durchschnittsverbrauch: {verbrauch_pro_100km:.2f} Liter/100km")
print(f"Kosten pro 100km: {kosten:.2f} Euro")
