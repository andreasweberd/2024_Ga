def avg(i):
    aTemps = []
    for x in range(i):
        aTemps.append(float(input("Temperatur eingeben: ")))
    print(f'Temperaturdurchschnitt: {str(sum(aTemps)/len(aTemps))}')

avg(3)