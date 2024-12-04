
# set

st=set() #set,   # duplicates not allowed , doesn't support indexing,

st={10,20,30,10,20,30}  

print(st)



# list to set convert

colors=["red","greeen","yellow"]     # input=[]

set_element=set(colors)
print(set_element)                  # output => {'red', 'greeen', 'yellow'}




#add()

colors={"red","green","blue"}

colors.add("yellow")

print(colors)



# intersection()

st1={10,20,30,40,50}

st2={10,20,60,70,80,40}

intersection_set=st1.intersection(st2)

print(intersection_set)



#union

union_element=st1.union(st2)

print(union_element)



#difference()

differnce_element=st1.difference(st2)

print(differnce_element)



#remove()

st1.remove(30)

print(st1)



#issubset()

st1={10,20,30,40,50}

st2={10,20,50,30,80,40}

print(st1.issubset(st2))



#issuperset()

print(st2.issuperset(st1))


# symmetric_difference()

print(st1.symmetric_difference(st2))



# update()

st1.update(st2)

print(st1)



text="this is a test to remove duplicate word this test is simple "

text2="this simple test remove duplicate word "


#remove repeated words

words=text.split(" ")

print(set(words))



# check text is created by text2

word1=text.split(" ")

word2=text2.split(" ")

print(set(word1).issubset(set(word2)))

