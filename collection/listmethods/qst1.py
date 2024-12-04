# rotates k times
# arr=[100,200,300,400,500] / k=1 output=> [500,100,200,300400]

arr=[100,200,300,400,500]

k=int(input("enter the times => "))

for i in range(1,k+1):

    popped_element=arr.pop()#500

    arr.insert(0,popped_element)

print(arr)


