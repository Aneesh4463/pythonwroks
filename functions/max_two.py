# create a function max_two with two parameter num1, num2 return largest number

def max_two(num1,num2):

    max_number=max(num1,num2)

    print(f"largest number is {max_number}")

    return 

max_two(12,14)

#OR

def max_two(num1,num2):

    return num1 if num1>num2 else num2

print(max_two(100,200))