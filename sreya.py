email=input("enter your email:-")
if email>="a" and email<="z":
    print(email)
password=int(input("enter the  password:-"))
if password>=0:
    username=input("enter the username:-")
    print("shreya")
    if username>="a" and username<="z":
        date=int(input("enter your birthdate:-"))
        print(25/4/2005)
        if date>=1 and date<=31:
            month=int(input("enter the birthmonth"))
            if month>0 and month<=12:
                year=int(input("enter the birthyear"))
                if year>0:
                    gender=input("enter your birthgender:-")
                    if gender=="femal" or "male":
                        login=input("do you want to login:-")
                        if login=="yes":
                            print("your facebook accout is successful creat")
                        else:
                            print("invalid")
                    else:
                        print("error")
                else:
                    print("unsussessful")
            else:
                print("not done")
        else:
            print("shreya")
    else:
        print("stop")
else:
    print("not")