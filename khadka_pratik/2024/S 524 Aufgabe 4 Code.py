n = int(input("Anzahl der Bilder eingeben: "))  
i = 0 

while i < n:
    h = int(input(f"Höhe Bilder {i+1}: ")) 
    b = int(input(f"Breit Bilder {i+1}: ")) 
    ft = int(input(f"Farbetief Bilder{i+1}: "))  

    g = b * h * ft 
    by = g / 8  
    mibi = by / (1024 * 1024)  
    print(f"Größe für Bilder {i+1} in MiB: {mibi}")  
    i += 1  
