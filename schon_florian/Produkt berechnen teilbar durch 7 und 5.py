def berechnung(x):
    i = 1
    produkt = 1
    while (i<=x):
        if (i % 5==0 and i % 7==0):
            produkt = produkt * i
        i = i+1
    if (produkt ==1):
        print('In diesem Bereich waren keine Zahlen, welche durch 5 und 7 teilbar sind')

    else:
        print('Das Produkt aller Zahlen von 1 bis', x ,' die durch 5 und 7 teilbar sind ist:', produkt)

#Test Eingabe
berechnung(35)

berechnung(70)

berechnung(276)