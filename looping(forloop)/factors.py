# print factors of a number => eg: 6=> 1.2.3.6

number=int(input(" enter the value => ")) #6

for i in range(1,number+1): # 1       2         3         4       5         6

    if number%i==0:         #6%1==0  6%2==0   6%3==0    6%4==0   6%5==0     6%6==0

        print(i)            #1        2         3         !=      !=           6
