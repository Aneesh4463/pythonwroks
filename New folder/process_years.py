
years_path="C:\\Users\\User\\Desktop\\pythonworksss\\collection\\file\\years.txt"

century_path="C:\\Users\\User\\Desktop\\pythonworksss\\collection\\file\\century.txt"

leap_year_path="C:\\Users\\User\\Desktop\\pythonworksss\\collection\\file\\leap_year.txt"

f_reads=open(years_path,"r")

is_century=open(century_path,"w")

is_leap=open(leap_year_path,"w")


for years in f_reads:

    years=int(years)

    if years%100==0:

        is_century.write(str(years)+"\n")

    if years%100==0 and years%400==0 or years%100!=0 and years%4==0:

        is_leap.write(str(years)+"\n")

f_reads.close()

is_century.close()

is_leap.close()


# or use function


years_path="C:\\Users\\User\\Desktop\\pythonworksss\\collection\\file\\years.txt"

century_path="C:\\Users\\User\\Desktop\\pythonworksss\\collection\\file\\century.txt"

leap_year_path="C:\\Users\\User\\Desktop\\pythonworksss\\collection\\file\\leap_year.txt"

f_reads=open(years_path,"r")

is_century=open(century_path,"w")

is_leap=open(leap_year_path,"w")



    



