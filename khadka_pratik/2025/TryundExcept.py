def checknum(num):
    if isinstance(num,float):
        return "Nummer ist dezimal"
    elif isinstance(num, int):
        return "Nummer ist ganz"

try: 
    num1 = input("Bitte ein Zahl eingeben: ")
    if '.' in num1:
        num1 = float(num1)
    else:
        num1 = int(num1)
        
    print(checknum(num1))
except ValueError:
    print("Es ist ein Fehler aufgetreten")
