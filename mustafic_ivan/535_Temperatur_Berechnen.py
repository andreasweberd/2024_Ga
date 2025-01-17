def getAvg(arr):
    return sum(arr)/len(arr)

inputArr = []
inCount = int(input('Wie viel Temperaturen mochten sie eingeben: '))

for i in range(0, inCount):
    inputArr.append(int(input('Temperatut eingeben: ')))

print(f'Die durschshnitt Temperatur ist {getAvg(inputArr)} Grad Celsius')
