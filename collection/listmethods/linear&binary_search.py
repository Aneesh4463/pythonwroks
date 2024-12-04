#searching => linear search ,binary search

#linear search

arr=[2,4,6,8,3,7]

search_element=int(input("enter the number => "))

is_present=False

for i in range(0,len(arr)):

    if arr[i]==search_element:

        is_present=True
        
        break

print(is_present)


# binary search

# =>search element set
# => sort array
# => set low,upp
# => find mid
# => case1,2,3

arr=[6,4,7,10,12,45]

arr.sort()

search_elemenet=int(input("enter the value =>"))

low=0

upper=len(arr)-1

is_present=False

while(low<=upper):

    mid=(low+upper)//2

    if search_elemenet==arr[mid]:

        is_present=True

        break

    elif search_elemenet<arr[mid]:

        upper=mid-1

    elif search_elemenet>arr[mid]:

        low=mid+1
        
print(is_present)