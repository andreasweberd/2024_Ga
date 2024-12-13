def berechneprodukt(endwert):
    produkt = 1
    for i in range(1, endwert + 1):
        if i % 5 == 0 or i % 7 == 0:
            produkt *= i
    return produkt

endwert = 100
print(berechneprodukt(endwert))
