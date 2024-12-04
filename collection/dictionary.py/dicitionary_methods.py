# employee id, name, department, age, salary

employee={"id":"12334","name":"hari","salary":35000,"department":"hr","age":32}



# get(key) : invalid key return none | valid key anel return 

print(employee.get("depatment"))                   # out => none



# return all keys => keys()                     

for k in employee.keys():

    print(k)                                       # out=> id, name, salary, department, age




# fetch all values => values()

for v in employee.values():

    print(v)                                       # out => 12334, hari, 35000, hr, 32



# fetch key and values => items()

for k,v in employee.items():

    print(k,v)                                    # out =>  id 12334, name hari, salary 35000, department hr, age 32



