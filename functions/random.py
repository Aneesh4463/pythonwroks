#create a function random number (start,end,step)
#print number from start to end
#random_number(1,7,2) => 1,3,5
#use while loop

def random_number(start,end,step=1):

    while start<=end:

        print(start)

        start=start+step

random_number(1,7,2)

