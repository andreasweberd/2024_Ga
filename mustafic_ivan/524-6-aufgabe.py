maxNum = int(input('Maximale ziffer: '))
summe = 0

for i in range(1, maxNum):
    if i % 5 == 0 and i % 7 == 0:
        summe += i

print('Summe:', summe)
