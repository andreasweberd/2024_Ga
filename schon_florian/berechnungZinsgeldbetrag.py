def berechnungZinsgeldbetrag():
    geldbetrag = int(input("Gib den Geldbetrag  an "))
    zinssatz = int(input("Gib den Zinssatz als ganze Zahl an "))
    zinsgeldbetrag = geldbetrag * zinssatz / 100
    return (zinsgeldbetrag)

print("Dein Zinsgeldbetrag beträgt ",berechnungZinsgeldbetrag() ," €")