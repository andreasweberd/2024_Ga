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