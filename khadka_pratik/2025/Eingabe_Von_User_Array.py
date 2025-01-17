def eingabe(arr):
    n = int(input("Wie viel Temperaturwerte möchte Sie eingeben?"))
    for i in range(n):
        temp = float(input(f"Bitte Temperaturwerte {i+1} geben:"))
        arr.append(temp)

array = []
eingabe(array)



total = sum(array)

durchschnitt = total / len(array)
print("Die Eingabe sind: ", array)
print("Durchschnittliche Temperatur: ")
print(durchschnitt)

        
