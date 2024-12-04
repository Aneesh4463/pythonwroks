# read start end
# print number from start to end


start=int(input("enter the value => ")) #5

end=int(input("enter the limit => "))   #10

for num in range(start,end+1):  #[5, 6, 7, 8, 9, 10]

    is_prime=True

    for i in range(2,num):  #[2,5]=(2,4) read

        if num%i==0:    #5%i==0

         is_prime=False

         break

    if is_prime==True:
   
        print(num)
