#armstrong => eg: 153=1^3+5^3+3^3=153

num=int(input("enter the value => "))

orginal_number=num

digit_count=len(str(num))

total=0

while(num!=0):

    digit=num%10

    armstrong=digit**digit_count

    total=total+armstrong

    num=num//10

if total==orginal_number:

    print(f"{orginal_number} is armstong")

else:

    print(" not a armstrong ")




    # another method


# print("armstrong" if total==orginal_number else "not a armstrong")