#   0   
#   0   1
#   0   1   1
#   0   1   1   2
#   0   1   1   2   3
#   0   1   1   2   3   5
#   0   1   1   2   3   5   8

for row in range(1,8):

    for col in range(1,row+1):

        print(col,end="\t")
    
    print()

