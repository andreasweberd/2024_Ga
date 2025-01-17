

def rechner(km,ks):
    dverbrauch_real = float(ks/km)
    preisproliter = 1.5
    #rechnen pro 100km
    dverbrauch_100km = float (dverbrauch_real * 100)
    print(("Pro 100Km wird " + str(dverbrauch_100km) + "L verbraucht."))
    total_preis = float(preisproliter*ks)
    print("Für "+str(ks) + "L wird es " + str(total_preis) +"EURO kosten")

try:    
    gefahr_km = float(input("Bitte die gefahrenen Kilometer eingeben: "))
    gefahr_ks = float(input("Biite getankene Menge eingeben: "))    
    rechner(gefahr_km,gefahr_ks)
except: 
    print("Joe Mama")
