# 1

# 2     2

# 3     3   3

# 4     4   4   4

# 5     5   5   5   5

for row in range(1,6): #[1,2,3,4,5] 2                       3

    for col in range(1,row+1): # col (1,row+1)(1,3) 1,2     col(1,4) 1 2 3

        print(row,end="\t") #row 2 2                          row 3 3 3

    print()