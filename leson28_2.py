sum=0
count=0
while True:
    s=input("Введите числа ")
    if s=="stop":
        break
    sum+=int(s)
    count+=1
l=sum/count
print(l)