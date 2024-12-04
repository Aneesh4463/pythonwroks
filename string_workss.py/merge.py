# text="PQRS"  #req output=> PAQBRCSD
# text2="ABCD"


# text1=input("enter the word: ")

# text2=input("enter the word: ")

# new_text=""

# if len(text1)==len(text2):
 
#  for i in range(0,len(text1)):
#     for j in range(0,len(text2)):
#         new_text+=text1[i]+text2[i]
#         break
#  print(new_text)
# else:
#    print("invalid string---make sure both the words have same number of characters")

text1="pqrs"
text2="abcd"
new_text=""
for i in range(0,4):
    
    new_text+=text1[i]+text2[i]

print(new_text)

