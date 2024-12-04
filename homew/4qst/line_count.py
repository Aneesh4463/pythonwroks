# write a python program that reads a file and print the total number of lines in the file

f=open("C:\\Users\\A S U S\\Desktop\\pythonworks\\homew\\4qst\\words.txt","r")

words=[]

count=0

for w in f:

    words.append(w.rstrip("\n"))

    count+=1

print(count)

f.close()