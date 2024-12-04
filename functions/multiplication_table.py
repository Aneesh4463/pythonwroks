# create multipilcation table of given n number

def multipilcation(num1,n):

    for i in range(1,n+1):

        result=num1*i

        print(f"{num1} x {i}= {result}")

        
    
multipilcation(3,10)

# or not given n value we already set a value

def multipilcation(num1,n=10):

    for i in range(1,n+1):

        result=num1*i

        print(f"{num1} x {i}= {result}")

        
    
multipilcation(3)