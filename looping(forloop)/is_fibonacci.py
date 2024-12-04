# check the number fibonacci series

number=int(input("enter the number => "))

pre=0

curr=1

is_fibno=False

for i in range(1,number+1):

    next=pre+curr

    pre=curr

    curr=next

    if number==next:

        is_fibno=True

        break

print(is_fibno)