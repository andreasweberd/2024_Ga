def berechne_uebertragungszeit(datenmenge_mb, uebertragungsrate_kbps):
    datenmenge_bit = datenmenge_mb * 8000000  # Datenmenge in Bits
    uebertragungsrate_mbps = uebertragungsrate_kbps / 1000  # Umrechnung Kbit/s in Mbit/s
    dauer_sekunden = datenmenge_bit / (uebertragungsrate_mbps * 1000000)  # Berechnung in Sekunden
    dauer_minuten = dauer_sekunden / 60  # Umrechnung in Minuten
    return dauer_minuten

datenmenge = float(input("Bitte geben Sie die Datenmenge in Megabyte (MB) ein: "))
uebertragungsrate = float(input("Bitte geben Sie die Übertragungsrate in Kilobit pro Sekunde (Kbit/s) ein: "))

zeit_minuten = berechne_uebertragungszeit(datenmenge, uebertragungsrate)

print(f"Die Übertragung dauert {zeit_minuten:.2f} Minuten.")
