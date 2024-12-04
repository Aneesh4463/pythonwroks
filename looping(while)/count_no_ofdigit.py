#write a program to count the number of digits in a given number using whileloop

value=int(input("enter the value "))

i=1

count=0

while(i<=value):
    
    print(i)

    count=count+1

    i=i+1
    
print(f"count => {count}")