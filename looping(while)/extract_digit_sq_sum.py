# extract digit square sum

num=int(input(" enter the value => "))

total=0

while(num!=0):

    digit=num%10

    digit_square=digit**2

    total=total+digit_square

    num=num//10

print(total)