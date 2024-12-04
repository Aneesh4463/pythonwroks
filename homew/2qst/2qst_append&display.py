# create a program that append user input to an existing file and 
# then display the entire content of th file

f=open("C:\\Users\\A S U S\\Desktop\\pythonworks\\homew\\qst2\\2existing_file.txt","a")

name=["ronaldo","messi","dolu","bolu","bheem"]

for n in name:

    f.write(n+"\n")

f.close()