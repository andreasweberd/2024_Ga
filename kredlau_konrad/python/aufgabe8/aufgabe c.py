def berechne_zinsen(geldbetrag, zinssatz):
    zinsbetrag = geldbetrag * (zinssatz / 100)
    return zinsbetrag

geldbetrag = float(input("Bitte geben Sie den Geldbetrag in Euro ein: "))
zinssatz = float(input("Bitte geben Sie den Zinssatz in Prozent ein: "))

zinsbetrag = berechne_zinsen(geldbetrag, zinssatz)

print(f"Der Zinsbetrag beträgt {zinsbetrag:.2f} Euro.")
