
# print character count

text="ABBACB"

chara_count={}

for ch in text:

    if ch in chara_count:

        chara_count[ch]+=1

    else:

        chara_count[ch]=1

print(chara_count)



#another method


character_frequency={ ch:text.count(ch)  for ch in text }


print(character_frequency)





# print non recursive elements

for k,v in character_frequency.items():


    if v==1:
        

        print(k)





#COMPERHENSION METHOD using


non_recursive_character=[ k  for k,v in character_frequency.items()  if v==1 ]


print(non_recursive_character)


# first recursive charcater  

# for k,v in character_frequency.items():

#     if v>1:

#         print(k)

#         break