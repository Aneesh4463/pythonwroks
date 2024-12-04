# write a python program to find second largest element in list

lst=[1,2,3,5,7,4,8,9,10]

lst.sort()

largest=0

for i in range(0,len(lst)-1):

    j=i+1

    if lst[i]<lst[j] :

        largest=lst[j]

print(lst[i])




