datenmengeInMB = int(input("Datenmenge in MB: "))
datenuebertragungsrateInKbitProSekunde = float(input("Datenübertragungsrate in Kbit/s: "))
datenMengeIKbit = datenmengeInMB*8000
uebertragungsdauerInMinuten = (datenMengeIKbit/datenuebertragungsrateInKbitProSekunde)/60
print("Übertragungsdauer in Minuten: "+str(uebertragungsdauerInMinuten))