num=int(input("enter the number"))
a=num%10
b=(num//10)%10
c=(num//100)%10
d=(num//1000)%10
new_number=(a*1000)+(b*100)+(c*10)+(d*1)
if num>0:
    print(new_number)
else:
    print("wrong")