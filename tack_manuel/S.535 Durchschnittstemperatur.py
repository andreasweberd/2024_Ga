def userInput():
    aTemps = []
    try:
        while(True):
            aTemps.append(float(input("Temperatur eingeben: ")))
    except ValueError:
        print("Der eingegebene Wert ist keine Zahl. Es wird der Durchschnitt der bisher eingegeben Werte zurückgegeben.")
    finally:
        avg(aTemps)

def avg(aTemps):
    try:
        print(f'Temperaturdurchschnitt: {str(sum(aTemps)/len(aTemps))}°C')
    except ZeroDivisionError:
        print("Es wurden keine gültigen Werte angegeben.")

userInput()