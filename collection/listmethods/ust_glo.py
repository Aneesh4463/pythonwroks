
#input:                                             output:
# arr=[100,200,300,400,500,600,700,800]                 result=[100,800,300,600,500,400,700,200]
#       0   1   2   3   4   5   6   7

# logic: odd_postion_element= [200,400,600,800]
#        reversed_odd_postion_element= [800,600,400,200]
#        insert_this elment into odd_postion




arr=[100,200,300,400,500,600,700,800] 

odd_postion_elemenet=[ arr[i]  for i in range(0,len(arr))  if i%2!=0 ]

print(odd_postion_elemenet)

for i in range(1,len(arr),2):

    element=odd_postion_elemenet.pop()

    arr[i]=element

print(arr)



#enumerates (iterable) => return index & numebr 
# for inex,number in enumerate(arr):

#     print(inex,number)




#another method

odd_postion_elemenet=[ number for index,number in enumerate(arr) if index%2!=0 ]

odd_postion_elemenet.reverse()

print(odd_postion_elemenet)

for index,number in enumerate(odd_postion_elemenet):

    arr[index+1]=number

print(arr)


 


