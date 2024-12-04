# duplicate numbers

arr=[1,2,2,2,1,4,5,66,66]

arr.sort()

duplicate_num=[]

for i in range(0,len(arr)-1):

    j=i+1

    result=arr[j]-arr[i]

    if result==0:

        if arr[i] not in duplicate_num:

            duplicate_num.append(arr[i])

print(duplicate_num)

