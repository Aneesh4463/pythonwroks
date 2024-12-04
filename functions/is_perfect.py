
def is_perfect_number(num):

    total=0

    for i in range(1,num):
        
        if num%i==0:

            total=total+i

    print("perfect number" if total==num else "not perfect")


is_perfect_number(5)