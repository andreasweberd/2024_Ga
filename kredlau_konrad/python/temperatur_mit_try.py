def durchschnittstemperatur(i):
    Temperaturliste = []
    for x in range(i):
        while True:
            try:
                temperatur = float(input("Temperatur eingeben: "))
                Temperaturliste.append(temperatur)
                break
            except ValueError:
                print("Das war keine gültige Zahl. Bitte erneut versuchen.")
    try:
        durchschnitt = sum(Temperaturliste) / len(Temperaturliste)
    except ZeroDivisionError:
        print("Keine Temperaturen eingegeben.")
        durchschnitt = None
    finally:
        if durchschnitt is not None:
            print(f'Der Durchschnittwert aller Temperaturen: {durchschnitt}')
        else:
            print("Es konnten keine korrekten Durchschnittswerte berechnet werden.")

# Wie viele Durchschnitte sollen berechnet werden?
durchschnittstemperatur(5)
