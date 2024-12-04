#lcm of number

num1=int(input("enter the value => "))  #3

num2=int(input("entre the value => "))  #4

max_num=max(num1,num2)  #4

for i in range(max_num,(num1*num2)+1,max_num):      #(4,13,4)

                                                         #+4step

    if i%num1==0 and i%num2==0:     #(4%3==0) and (4%4==0) =F | (8%3==0)and(8%4==0)=F | (12%3==0)and(12%4==0)=T


        print(i)                    #not print                | not print |           | print i=12 stop

        break






