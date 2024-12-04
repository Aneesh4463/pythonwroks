

arr=[10,20,30,40,2,3]  #out => {10:100,20:400....}
     
result={}

for num in arr:

    sqaure=num**2

    result[num]=sqaure

print(result)



#another method

# result={key:value  iteration  condition}      =>   dicitionary comphersion

result={ num:num**3 for num in arr}

print(result)




# another method

# arr=[10,20,30,40,2,3]

# arr_dicitionary={}

# for k in arr:

#     if k in arr_dicitionary:

#         arr_dicitionary[k]+=k

#     else:

#         arr_dicitionary[k]=k**2

# print(arr_dicitionary)






