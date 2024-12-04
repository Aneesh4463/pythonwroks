#5=1*2*3*4*5 = 120

number=int(input("enter the value => ")) #3

fact=1

for num in range(1,number+1,1):     #(1,4,1)

    fact=num*fact                      #(1*2*3*)

print(fact)