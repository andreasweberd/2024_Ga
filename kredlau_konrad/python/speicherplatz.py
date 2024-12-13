def speicherplatzberechnen(menge, hoehe, breite, farbtiefe):
    mengeBildpunkte = hoehe * breite
    speicherplatzBild = mengeBildpunkte * farbtiefe
    speicherplatzGesamtByte = speicherplatzBild / 8
    speicherplatzBildMiB = speicherplatzGesamtByte / (1024 * 1024)
    speicherplatzGesamtMiB = speicherplatzBildMiB * menge
    
    return speicherplatzGesamtMiB

# Werte eintragen...
menge = 10
hoehe = 1920  
breite = 1080  
farbtiefe = 24

speicherbedarf = speicherplatzberechnen(menge, hoehe, breite, farbtiefe)
print(f"Der Gesamt-Speicherbedarf für die Bilder beträgt {speicherbedarf:.2f} MiB")
