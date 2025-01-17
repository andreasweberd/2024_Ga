total = 0
count = 0

while True:
    try:
        num = float(input("Gib eine Zahl ein: "))
        total += num
        count += 1
    except ValueError:
        if count == 0:
            print("Keine gültigen Zahlen eingegeben. Durchschnitt kann nicht berechnet werden.")
        else:
            average = total / count
            print(f"Falsche Eingabe. Der Durchschnitt der eingegebenen Zahlen ist: {average:.2f}")
        break

