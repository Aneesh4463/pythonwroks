# Read three number and sorted order

num1=int(input("enter the first number => "))

num2=int(input("enter the second number => "))

num3=int(input("enter the third number => "))

if num1>num2 and num1>num3:

    if num2>num3:

        print(num1,num2,num3)

    else:

        print(num1,num3,num2)

elif num2>num1 and num2>num3:

    if num1>num3:

        print(num2,num1,num3)
    
    else:

        print(num2,num3,num1)

elif num3>num2 and num3>num1:

    if num2>num1:

        print(num3,num2,num1)
    else:

        print(num3,num1,num2)

elif num1==num2==num3:

    print("both are same number")

else:

    print("invalid")
