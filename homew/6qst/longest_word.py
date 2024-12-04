# write aprogram that find and prints the longest word in a text file.

f=open("C:\\Users\\A S U S\\Desktop\\pythonworks\\homew\\6qst\\word.txt","r")

word=[]

for w in f:

    word.append(w.rstrip("\n"))

print(word)

for l in word:
    
    words=len(l)

    print(words,l)
    



    

    

