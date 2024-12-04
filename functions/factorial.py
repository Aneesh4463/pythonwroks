# create a factorial(num)

def factorial(num):

    fact=1

    for i in range(1,num+1):

        fact=fact*i

    return fact #print(fact)

print(factorial(5))