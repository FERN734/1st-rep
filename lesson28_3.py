count=0
max_number=999
max_count=0
while True:
    s=input("Введите число ")
    if s=="stop":
        break
    count+=1
    if max_number<int(s):
        max_number=int(s)
        max_count=count
print(max_number,max_count)