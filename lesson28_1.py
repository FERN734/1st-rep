sum=0
while True:
    product=float(input("Введите цену "))
    if product<0:
        break
    if product>1000:
       product*=0.95
    sum+=product
print(sum)

    
    