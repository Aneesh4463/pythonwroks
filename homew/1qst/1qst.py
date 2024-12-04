# write a program to take input from the user and write it to file
# then, read the content from the file and display it


f_read=open("C:\\Users\\A S U S\\Desktop\\pythonworks\\homew\\1qst_user.txt","r")

name=[]

for n in f_read:

    name.append(n.rstrip("\n"))

print((name))

f_write=open("C:\\Users\\A S U S\\Desktop\\pythonworks\\homew\\1qst_write.txt","w")

for w in name:

    f_write.write(w+"\n")

f_write.close()
