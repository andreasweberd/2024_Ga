geldbetrag = int(input("Geldbetrag: "))
zinssatz = float(input("Zinssatz: "))

zinsgeldbetrag = geldbetrag + geldbetrag * (zinssatz/100)

print(zinsgeldbetrag)