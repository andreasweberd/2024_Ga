a = int(input('Erste Zahl eingeben: '))
b = int(input('Zweite Zahl eingeben: '))
c = int(input('Dritte Zahl eingeben: '))
losung = ''

while True:
    if a > 0 and b <= 0 and c <= 0:
        losung = 'erste'
        break
    if b > 0 and a <= 0 and c <= 0:
        losung = 'zweite'
        break
    if c > 0 and b <= 0 and a <= 0:
        losung = 'dritte'
        break
    a -= 1
    b -= 1
    c -= 1

print('Die', losung, 'eingabe ist die grosste zahl')
