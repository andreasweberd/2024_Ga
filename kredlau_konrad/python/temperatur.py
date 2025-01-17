def durchschnittstemperatur(i):
    Temperaturliste = []
    for x in range(i):
        Temperaturliste.append(float(input("Temperatur eingeben: ")))
    print(f'Der Durchschnittwert aller Temperaturen: {str(sum(Temperaturliste)/len(Temperaturliste))}')


# Wie viele Durchschnitte sollen berechnet werden?
durchschnittstemperatur(5)