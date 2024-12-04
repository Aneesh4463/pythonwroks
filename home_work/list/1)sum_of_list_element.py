# write a python program to find the sum of all elements in a list 

lst=[1,2,3,4,5,6]

length=len(lst)

result=0

for i in range(0,length):

    result=lst[i]+result

print(result)