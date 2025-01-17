

n = int(input("Endwert bitte einbegen: "))
i = 1
prod = 1
while(i <=n):
    if i%5==0  and i%7==0 :
        print (i)
        prod = i*prod

    i +=1

print(prod)
