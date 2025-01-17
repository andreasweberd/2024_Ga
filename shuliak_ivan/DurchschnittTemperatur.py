temperaturen = []

for i in range(3):
    temp = float(input(f"Eingabe temperatur{i+1}: "))
    temperaturen.append(temp)

durchschnitt = sum(temperaturen) / len(temperaturen)

print(f"Durchschnitt: {durchschnitt}")