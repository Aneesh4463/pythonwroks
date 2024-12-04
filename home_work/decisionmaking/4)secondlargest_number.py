# Read three number print second largest number

num1=int(input("enter the first number => "))

num2=int(input("enter the second number => "))

num3=int(input("enter the third number => "))

if num1>num2 and num1>num3:

    if num2>num3:

        print(f"{num2} is the second last number")

    else:

        print(f"{num3} is the second last number")

elif num2>num1 and num2>num3:

    if num1>num3:

        print(f"{num1} is the second last number ")
    
    else:

        print(f"{num3} is the second last number")

elif num3>num2 and num3>num1:

    if num2>num1:

        print(f"{num2} is second last number")
    else:

        print(f"{num1} is the second last number")

elif num1==num2==num3:

    print("both are same number")

else:

    print("invalid")


