# print even number

start=int(input("enter the starting value => "))

end=int(input("enter the end value => "))

if start<end:
        
        for i in range(start,end+1,1):
              
            if i%2==0:
            
                print(f"{i} is even")

else:
        for i in range(start,end-1,-1):

            if i%2==0:
            
                print(f"{i} is even")

        

