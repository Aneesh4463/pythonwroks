# write a program check leapyear or not

year=int(input("enter year => "))

if (year%100!=0 and year%4==0 ) or (year%100==0 and year%400==0):

    print(f"{year} is a leapeyear")

else:

    print(f"{year} is not a leapyear")