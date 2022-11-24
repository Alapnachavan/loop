# Make a program that should do the following thing from 1 to 100.

#     Numbers that are divisible by 3, you have to print "Nav".

#     Numbers that are divisible by 7 so that "Gurukul" is printed.

#     Numbers that are divisible by both 3 and 7, print "NavGurukul" there.

#     If the number does not come in the above three cases then print the number only.

# i=1
# while i<=100:
#     if i%3==0:
#         print("Nav")
#     elif i%7==0:
#         print("Gurukul")
#     elif i%3==0 and i%7==0:
#         print("navgurukul")
#     else:
#         print(i)
#     i+=1

num=(input("enter the input"))
a=num.split()
print(a)
i=0
while i <len(num):
    if num[i]==num[i]:
        print(i*i)
    i=i+1
