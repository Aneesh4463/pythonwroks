# check the year is not a century

year=int(input("enter the year => "))

is_not_century=year%100

rem=is_not_century!=0
print(rem)