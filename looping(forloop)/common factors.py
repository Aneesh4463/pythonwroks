#2number common factors =>  10,20 => 1, 2, 5, 10

num1=int(input("enter the number => "))

num2=int(input("enter the number => "))


min_num=min(num1,num2)

# min_num=num1 if num1<num2 else num2


for i in range(1,num1+1,1):

    if num1%i==0 and num2%i==0:

        print(i) 