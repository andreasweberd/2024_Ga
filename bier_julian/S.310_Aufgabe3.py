#Aufgabe 3 a)

def berechne_uebertragungszeit(datenmenge_mb, uebertragungsrate_kbps):
    datenmenge_kbit = datenmenge_mb * 8 * 1024
    zeit_sekunden = datenmenge_kbit / uebertragungsrate_kbps
    zeit_minuten = zeit_sekunden / 60

    return zeit_minuten

datenmenge_mb = float(input("Gib die Datenmenge in MB ein: "))
uebertragungsrate_kbps = float(input("Gib die Datenübertragungsrate in kbit/s ein: "))
uebertragungszeit_minuten = berechne_uebertragungszeit(datenmenge_mb, uebertragungsrate_kbps)

print(f"Die benötigte Zeit für die Übertragung beträgt: {uebertragungszeit_minuten:.2f} Minuten")


#Aufgabe 3 b)

def berechne_nettolohn(bruttolohn):
    steuerklasse_1 = 0.30
    solidaritaetszuschlag = 0.055
    krankenversicherung = 0.146
    rentenversicherung = 0.025
    arbeitslosenversicherung = 0.026

    steuer_abzug = bruttolohn * steuerklasse_1
    soli_abzug = bruttolohn * solidaritaetszuschlag
    kv_abzug = bruttolohn * krankenversicherung
    rv_abzug = bruttolohn * rentenversicherung
    av_abzug = bruttolohn * arbeitslosenversicherung

    nettolohn = bruttolohn - (steuer_abzug + soli_abzug + kv_abzug + rv_abzug + av_abzug)
    return nettolohn

bruttolohn = float(input("Gib deinen Bruttolohn ein: "))

nettolohn = berechne_nettolohn(bruttolohn)

print(f"Dein Nettolohn beträgt: {nettolohn:.2f} Euro")


# Aufgabe 3 c)

def berechne_zins(betrag, zinssatz):
    return betrag * (zinssatz / 100)

betrag = float(input("Gib den Geldbetrag ein: "))
zinssatz = float(input("Gib den Zinssatz (in Prozent) ein: "))

zinsbetrag = berechne_zins(betrag, zinssatz)

print(f"Der Zinsertrag beträgt: {zinsbetrag:.2f} Euro")

