# find common element | common element without using "in" | output =13,20,8

arr=[10,13,8,11,20]

arr2=[2,20,8,7,13]

for i in range(0,len(arr)):

    for j in range(0,len(arr2)):

        if arr[i]==arr2[j]:

            print(arr[i])

            
 # another method


arr1=[10,13,8,11,20]

arr2=[2,20,8,7,13]

arr1.sort()

arr2.sort()

p1=0

p2=0

while(p1<=len(arr1)-1 and p2<=len(arr2)-1):

    if arr1[p1]==arr2[p2]:

        print(arr1[p1])

        p1+=1

        p2+=1
    
    elif arr1[p1]<arr2[p2]:

        p1+=1

    elif arr2[p2]<arr1[p1]:

        p2+=1







