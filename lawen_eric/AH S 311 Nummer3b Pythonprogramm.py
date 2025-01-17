bruttolohn= float(input ("Burrotlohn: "))
steuerklasse1 = 0.30
solidaritätszuschlag = 0.055
krankenversicherung = 0.146
rentenversicherung = 0.186
arbeitslosenversicherung = 0.026

def berechnung(bruttolohn, steuerklasse, soli, kv, rv, alv):
    bruttolohn += steuerklasse*bruttolohn
    bruttolohn += soli*bruttolohn
    bruttolohn += kv*bruttolohn
    bruttolohn += rv*bruttolohn
    bruttolohn += alv*bruttolohn
    return bruttolohn

print(berechnung(bruttolohn,steuerklasse1,solidaritätszuschlag,krankenversicherung,rentenversicherung,arbeitslosenversicherung))

