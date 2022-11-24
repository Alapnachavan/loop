# n=input("enter the number:")
n=5
for x in range(n,0,-1):
    for y in range(n,0,-1):
        if x>=y:
            print(y,end="")
        else:
            print("",end="")
    print()