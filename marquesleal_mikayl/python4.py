# Eingabe
anzahl_bilder = int(input("Anzahl der Bilder: "))
hoehe = int(input("Höhe (in Pixel): "))
breite = int(input("Breite (in Pixel): "))
farbtiefe = int(input("Farbtiefe (in Bits): "))

# Berechnung des Speicherbedarfs
speicherbedarf = (anzahl_bilder * hoehe * breite * farbtiefe) / (8 * 1024 * 1024)

# Ausgabe
print(f"Der Speicherbedarf beträgt {speicherbedarf:.2f} MiB")
