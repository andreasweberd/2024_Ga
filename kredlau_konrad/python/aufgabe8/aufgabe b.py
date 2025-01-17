def berechne_nettolohn(bruttolohn):
    lohnsteuer = bruttolohn * 0.30
    soli = lohnsteuer * 0.055
    krankenversicherung = bruttolohn * 0.146
    rentenversicherung = bruttolohn * 0.186
    arbeitslosenversicherung = bruttolohn * 0.025
    
    abzüge = lohnsteuer + soli + krankenversicherung + rentenversicherung + arbeitslosenversicherung
    nettolohn = bruttolohn - abzüge
    
    return nettolohn

bruttolohn = float(input("Bitte geben Sie Ihren Bruttolohn in Euro ein: "))

nettolohn = berechne_nettolohn(bruttolohn)

print(f"Ihr Nettolohn beträgt {nettolohn:.2f} Euro.")
