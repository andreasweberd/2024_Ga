d_menge = float(input("Bitte Datenmenge in MB geben"))
d_rate = float(input("Bitte übertragungs rate in Kbits/s geben"))


einkbitprosek = float(1/d_rate)
d_rate = d_rate * 1000
d_rate = float(d_rate/(8*1000*1000))
zeit = float(d_menge/d_rate)
minuten = float(zeit/60)
print(str(minuten)  + "Minuten")
