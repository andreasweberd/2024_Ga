total = 0
try:
    totalnums = int(input("Wie viel Zahlen möchten Sie eingeben?"))

#try:
    for i in range(totalnums):
        num = int(input(f"Bitte Nummer {i+1} eingeben: "))
        total+=num
        
    avg = float (total/totalnums)
    print(avg)
    
except:
    print("Es ist ein Fehler aufgetreten")
