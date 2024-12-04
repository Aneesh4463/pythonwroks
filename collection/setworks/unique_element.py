arr=[100,10,10,20,30,40,50,40]

# create empty set

st=set()

# fetch number from array

for num in arr:

    #add num to set

    st.add(num)

#display set

print(st)


st1={10,20,30,40,50}

st2={10,20,60,70,80}

intersection_set=st1.intersection(st2)

print(intersection_set)