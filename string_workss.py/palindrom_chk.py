# reversed the word using forloop

text=input("enter the word => ")

# hello=>index=01234
       #length=12345

reversed_str=""

length=len(text)-1  #5-1
 
for i in range(length,-1,-1):

    reversed_str+=text[i]

print("palindrome" if reversed_str==text else "not palindrome")