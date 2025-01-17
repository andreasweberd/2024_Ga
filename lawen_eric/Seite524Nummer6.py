endwert = int (100)

x = 1

i = 1

while i < endwert:
    i += 1
    if i % 5 == 0 and i % 7 == 0:
        x = x * i
    else:
        continue


print (x)