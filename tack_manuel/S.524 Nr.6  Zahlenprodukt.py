def produkt(Endwert):
    Startwert = 1
    Produkt = 1
    while(Startwert <= Endwert):
        if(Startwert % 5 == 0 and Startwert % 7 == 0):
            Produkt = Produkt * Startwert
        Startwert = Startwert + 1
    if Produkt == 1:
        return 0
    else:
        return Produkt

if __name__ == "__main__":
    print(produkt(10))
    print(produkt(100))
    print(produkt(1000))