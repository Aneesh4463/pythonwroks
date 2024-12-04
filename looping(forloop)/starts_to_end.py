# print all numbers from starts to end

starts=int(input("enter the value => "))

end=int(input("enter the end value => "))

if starts<end:
    
    for num in range(starts,end+1,1):

      print(num)

else:
   
   for num in range(starts,end-1,-1):
      
      print(num)
