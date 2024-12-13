endwert = int (100)

x = 1

i = 1

while i < endwert:
    if i % 5 == 0 and i % 7 == 0:
        i += 1
        x = x * i
    else:
        i += 1
        continue


print (x)