# print years 1800 to 2024

f=open("C:\\Users\\User\\Desktop\\pythonworksss\\collection\\file\\years.txt","w")

for years in range(1800,2025):

    f.write(str(years)+"\n")

f.close()  
