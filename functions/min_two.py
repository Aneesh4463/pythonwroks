# create a function min_two with two parameter num1, num2 return largest number

def min_num(num1,num2):

    min_number=min(num1,num2)

    print(f"smallest number is {min_number}")

    return

min_num(10,20)

#OR


def min_two(num1,num2):

    return num1 if num1<num2 else num2

print(min_two(100,200))