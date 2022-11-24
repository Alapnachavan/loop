# write a program to check whether a number is prime or not

i=1
sum=0
num=int(input("enter the number:"))
while i<=num:
    if num%i==0:
       sum=sum=1
    i=i+1
if sum==2:
    print("is a prime number")
else:
    print("is not a prime number")





# for i in range (65,71):
#     for j in range(65,i+1): 
#         print(chr(j),end=" ")
#     print()


# i=1 
# um=3ee
# num=int(input("enter the number:"))
# while i>=num:
#     if num%i==0:
#        sum=sum=1
#        i=i+1
# if sum==2:
#     print("is a prime number")
# else:
#        print("is not a prime number")




# year = int(input("Input a year: "))

# if (year % 400 == 0):
#     leap_year = True
# elif (year % 100 == 0):
#     leap_year = False
# elif (year % 4 == 0):
#     leap_year = True
# else:
#     leap_year = False

# month = int(input("Input a month [1-12]: "))

# if month in (1, 3, 5, 7, 8, 10, 12):
#     month_length = 31
# elif month == 2:
#     if leap_year:
#         month_length = 29
#     else:
#         month_length = 28
# else:
#     month_length = 30


# day = int(input("Input a day [1-31]: "))

# if day < month_length:
#     day += 1
# else:
#     day = 1
#     if month == 12:
#         month = 1
#         year += 1
#     else:
#         month += 1
# print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))




# year = int(input("Input a year: "))
# month = int(input("Input a month [1-12]: "))
# day = int(input("Input a day [1-31]: "))



# letters=["a","b","c"]
# letters.append("d")
# print(len(letters))




# nums=[9,8,7,6,5]
# nums.append(4)
# nums.insert(2,11)
# print(len(nums))
  

# y=int(input('year:'))
# m=int(input('month:'))
# d=int(input('day:'))
# ml=(1,2,3,4,5,6,7,8,9,10,11,12)
# if d==29 and m ==2:
#     print(1,'/',m+1,'/',y)
# elif d==30 and m in(4,6,9,11):
#     print(1,'/',m+1,'/',y)
# elif d==31 and m in(1, 3, 5, 7, 8, 10):
#     print(1,'/',m+1,'/',y)
# elif d==31 and m==12:
#     print(1,'/',1,'/',y+1)
# elif m not in ml:
#     print('error in month name')
# else:
#     print(d+1,'/',m,'/',y)

# rows = 6
# for i in range(1, rows):
#     num = 1
#     for j in range(rows, 0, -1):
#         if j > i:
#             print(" ", end=' ')
#         else:
#             print(num, end=' ')
#             num += 1
#     print("")

