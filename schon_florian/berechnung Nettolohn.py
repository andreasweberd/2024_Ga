def berechnungNettolohn():
    bruttolohn = int(input("Gib deinen Bruttolohn an "))
    abgaben = 0.3 + 0.055 + 0.073 + 0.093 + 0.013
    nettolohn = bruttolohn * (1-abgaben)
    return (nettolohn)

print ("Dein Nettolohn beträgt ",berechnungNettolohn())