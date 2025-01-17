def calculate_average_temperature():
    temperaturen = []

    for i in range(3):
        while True:
            try:
                temp = float(input(f"Eingabe temperatur{i + 1}: "))
                temperaturen.append(temp)
                break
            except ValueError:
                print("Fehler: Bitte geben Sie eine Zahl ein!")

    durchschnitt = sum(temperaturen) / len(temperaturen)
    print(f"Durchschnitt: {durchschnitt}")

    return durchschnitt


try:
    average = calculate_average_temperature()
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")