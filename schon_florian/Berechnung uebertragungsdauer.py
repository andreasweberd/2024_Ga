def berechneUebertragungsdauer():
    datenmenge = float(input("Gib die Datenmenge in Mb an "))
    uebertragungsrate = float(input("Gib die Übertragungsrate in Kbit/s an "))
    datenmengeKbit = datenmenge * 8 * 1000
    zeit = datenmengeKbit / uebertragungsrate
    return (zeit)

print ("Die Übertragungsdauer beträgt ", berechneUebertragungsdauer(), "Sekunden")