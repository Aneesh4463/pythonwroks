# find index of @

#slice text from 0:index of slice

test="vipinkumar@gmail.com"

index=test.index("@")

word=""

for i in range(0,index):

    word+=test[i]

print(word)

# or method 

test2="vipinkumar@gmail.com"

print(test[0:test.index("@")])


test1="vipinkumar@gmail.com"

index=test.index("@")


name=test[:index]

print(name)






