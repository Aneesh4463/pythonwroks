# sample1 :
# hw => arr=[1,3,4,5]
#find least +ve  missing integer 2

# sample2 :
# arr2=[1,2,3,5]  out = 4


arr=[1,3,4,5]

lenght=len(arr)

minimum=arr[0]

for i in range(0,lenght):

    if minimum>=arr[i]:

        minimum=arr[i]

print(minimum+1)


# another method

arr=[1,3,4,5]

arr.sort()


for i in range(0,len(arr)-1):

    j=i+1

    result=arr[j]-arr[i]

    if result!=1:

        print(arr[i]+1,"is missing number")

        break




