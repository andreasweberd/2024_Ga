gefahreneKm = float(input('Wie viel Kilometer sind sie gefahren: '))
kraftstofLrer = float(input('Wie viel Liter Kraftstoff haben sie getankt: '))
preisProLiter = float(input('Wie viel kostet ein Liter Kraftstoff: '))


averageFuelConsumption = (kraftstofLrer / gefahreneKm) * 100
preisProLiter = preisProLiter * averageFuelConsumption

print(f'Der durchschnittliche Kraftstoffverbrauch beträgt {averageFuelConsumption:.2f} Liter pro 100 km')
print(f'Die Kosten pro 100 km betragen {preisProLiter:.2f} Euro')