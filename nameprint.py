for row in range(6):
    for col in range(6):
        if col==0 or col==5 or (row==col and (col>0 and col<5)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
for row in range (7):
    for col in range (5):
        if col==2 or (row==0 or row==6) and col!=2:
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
for row in range (6):
    for col in range (4):
        if col==0 or (row==5 and col!=0):
            print("*",end=" ")
        else:
            print(end=" ")
    print()
print()        
for row in range (7):
    for col in range(6):
        if ((row==0 or row==3 or row==6)) or ((col==0 ) and (row!=0 and row!=3 and row!=6)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
for row in range (7):
    for col in range (5):
        if ((row==0 or row==3 or row==6) and (col>0 and col<4))or col==0 and (row>0 and row<3) or (col==4 and (row>3 and row<6)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
for row in range (7):
    for col in range(4):
        if col==0 or col==3 or (row==3 and (col>0 and col<4)):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
# for i in range (1,11):
    # print(i*"*")


# i=5
# while i>=0:
#     print(-i,end=" ")
#     i=i-1