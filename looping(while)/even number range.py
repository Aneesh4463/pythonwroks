#write a python program to print all even number between 1 & 50 using while loop

start=int(input("enter start number => "))

end=int(input("enter end number => "))

if start>end:
    start,end=end,start

i=start

while(i<=end):

    if i%2==0:

     print(i)
 
    i=i+1


