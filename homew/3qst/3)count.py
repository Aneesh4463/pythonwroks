# write a program to count the number of words in a given text file

f=open("C:\\Users\\A S U S\\Desktop\\pythonworks\\homew\\3qst\\count.txt","r")

words=[]

count=0

for w in f:

    words.append(w.rstrip("\n"))

    count+=1

print(count)

f.close()