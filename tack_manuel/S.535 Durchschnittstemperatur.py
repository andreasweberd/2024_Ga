def avg(i):
    aTemps = []
    try:
        for x in range(i):
            aTemps.append(float(input("Temperatur eingeben: ")))
    except ValueError:
        print("Der eingegebene Wert ist keine Zahl. Es wird der Durchschnitt der bisher eingegeben Werte zurückgegeben.")
    finally:
        try:
            print(f'Temperaturdurchschnitt: {str(sum(aTemps)/len(aTemps))}')
        except ZeroDivisionError:
            print("Es wurden keine gültigen Werte angegeben.")

avg(3)