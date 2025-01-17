def berechne_speichermenge(hoehe, breite, farbtiefe, menge):

  speichermenge_bit = hoehe * breite * farbtiefe * menge

  speichermenge_mibit = speichermenge_bit / (2**20)

  speichermenge_mib = speichermenge_mibit / 8

  return speichermenge_mib

hoehe = 1920  
breite = 1080
farbtiefe = 24
menge = 10

ergebnis = berechne_speichermenge(hoehe, breite, farbtiefe, menge)
print("Speichermenge:", ergebnis, "MiB")