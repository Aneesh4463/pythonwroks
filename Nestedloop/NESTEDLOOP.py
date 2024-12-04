
# good $$ afternoon     All

print("Good",end=" $$ ")       # \n => next line                

print("Afternoon",end="\t")  #\t => tab space

print("All")




#print pattern

#  c1   c2  c3
#  1 *    *   *
#  2 *    *   *
#  3 *    *   *
#  4 *    *   *
#  5 *    *   *
#  6 *    *   *
#  7 *    *   *

for row in range(1,8):

    for col in range(1,4):

        print("*",end="\t")                 #end use for tabspace 

    print()

