#prime number 
#logic=> exclude(1,number)

num=int(input("enter the number => "))          #5

is_prime=True

for i in range(2,num):         #   (2,8)=>[2,3,4]

    if num%i==0:            # 5%2==0 | 5%3==0 | 5%4==0 (not divisible or not equal)

       is_prime=False     #true

       break

print(is_prime)

    