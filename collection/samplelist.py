# input => list[2,3,4,5]
#output => 12,11,10,9

lst=[2,3,4,5]

sum=""

total=0

for j in lst:

    total+=j

for i in range(0,len(lst)):

    sum=total-lst[i]
    
    print(sum)