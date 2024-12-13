def berechne_speichermenge(hoehe, breite, farbtiefe, anzahl_bilder):

  speichermenge_bit = hoehe * breite * farbtiefe * anzahl_bilder

  speichermenge_mib = speichermenge_bit / (2**20)

  return speichermenge_mib


hoehe = 1920  
breite = 1080
farbtiefe = 24
anzahl_bilder = 10

ergebnis = berechne_speichermenge(hoehe, breite, farbtiefe, anzahl_bilder)
print("Speichermenge:", ergebnis, "MiB")