#extract digit and add the number ?    
#eg: 132=> 1+3+2=6

num=int(input("enter the number => "))

total=0

while(num!=0): #132!=0                  13                                          1

    digit=num%10    #132%10=2              13%10=3                                  1%10=1

    total=total+digit   #2+0=2              2+3=5                                      5+1=6

    num=num//10     #132//10=13.2=13               13//10=1.3=1                               1//10=0.1=0

print(total)


   