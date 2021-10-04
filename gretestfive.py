num1=int(input("enter the no"))
num2=int(input("enter the no"))
num3=int(input("enter the no"))
num4=int(input("enter the no"))
num5=int(input("enter the no"))
if num1>num2 and num1>num3 and num1>num4 and num1>num5:
    print("num1 is greter")
elif num2>num3 and num2>num4 and num2>num5 and num2>num1:
    print("num2 is greter")
elif num3>num4 and num3>num5 and num3>num1 and num3>num2:
    print("num3 is greter")
elif num4>num5 and num4>num1 and num4>num2 and num4>num3: 
    print("num4 is greter")
elif num5>num1 and num5>num2 and num5>num3 and num5>num4:
    print("num5 is greter")
else:
    print ("not") 