#exponent

def exponent(number,expo):

    result=number**expo

    print(result)

exponent(3,3)

#or return


def exponent(number,expo):

    return number**expo

print(exponent(3,3))

# or without given the exponent

def exponent(number,expo=2):

    return number**expo

print(exponent(3))