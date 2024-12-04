# print 7 fibonoacci number 

prev=0

curr=1

print(prev)

print(curr)

for i in range(1,6):

    next=prev+curr

    print(next)

    prev=curr

    curr=next


