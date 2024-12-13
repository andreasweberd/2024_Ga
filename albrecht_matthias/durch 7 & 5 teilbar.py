def berechne_produkt(n):

  produkt = 1

  for i in range(1, n+1):
    if i % 7 == 0 and i % 5 == 0:
      print(i)
      produkt *= i

  return produkt

n = 100
ergebnis = berechne_produkt(n)
print("Das Produkt aller Zahlen des Zahlenbereichs, welche durch 7 und durch 5 teilbar sind ist:", ergebnis)