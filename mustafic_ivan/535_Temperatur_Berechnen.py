def getAvg(arr):
    return sum(arr)/len(arr)

inputArr = []
inCount = int(input('Wie viel Temperaturen mochten sie eingeben: '))

for i in range(0, inCount):
    while True:
        try:
            inputArr.append(int(input('Temperatut eingeben: ')))
            break
        except Exception as error:
            print(f'{error} Bitte eine valide ziffer eingeben')

print(f'Die durschshnitt Temperatur ist {getAvg(inputArr)} Grad Celsius')