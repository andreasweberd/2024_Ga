def eingabe(arr):
    print("Bitte 3 Temperaturwerte eingabe")
    for i in range (3):
        temp = float( input(f"Bitte Temperaturwerte {i+1} geben: "))
        arr.append(temp)

array = []
eingabe(array)



total = sum(array)

durchschnitt = total / len(array)
print("Die Eingabe sind: ", array)
print("Durchschnittliche Temperatur: ")
print(durchschnitt)

        
