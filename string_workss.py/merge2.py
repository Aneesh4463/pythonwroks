#text=PQRSt     #req output=>PAQBRCS
#text2=ABC

text1="pqrs"

text2="abc"  

result=""

smallest= text1 if len(text1)<len(text2) else text2

largest= text1 if len(text1)>len(text2) else text2

for i in range(0,len(smallest)):

    result+=text1[i]+text2[i]

bal_text=largest[len(smallest):]

result+=bal_text

print(result)




