datenmenge = float(input("Datenmenge MB: "))
datenuebertragungsrate = float(input("Datenübertragungsrate Kbits/s: "))
ergebnis = (datenmenge*1000/datenuebertragungsrate)/60
print(f"Ergebnis: {ergebnis:.2f} Minuten")