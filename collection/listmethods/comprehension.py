# list comprehension



# syntax=> refernce=[return  loop  condition]                               
 
arr=[2,3,4,5,6,7,]


squares= [num**2  for num in arr ]                   # find sqaure of all number in array     mapping =all elements return (notexclued)           

print (squares)     



add_five= [num+5  for num in arr ]                   # add 5 to all number in array           mapping =all elements return (notexclued)

print (add_five)



even_number= [num  for num in arr  if num%2==0]      # find even numbers(conditon)            filter =only give filtered numbers (exclued)

print(even_number)



odd_number= [num  for num in arr if num%2!=0]        # find odd numbers(conditon)              filter =only give filtered numbers (exclued)

print(odd_number)



greater_th_5= [num  for num in arr  if num>5 ]       # find the number greater than 5          filter =only give filtered numbers (exclued)

print(greater_th_5)


new_list=[num+1 if num>5 else num-1 for num in arr]  # return num+1 if num>5 else num-1        mapping=return all elements
print(new_list)




# words starting with vowels

text=["apple","orange","iphone","potatto","tomattoes"]

vowels=[w for w in text if w[0] not in ["a","e","i","o","u"]]

print(vowels)

consonant_words=[w for w in text if w[0] not in ["a","e","i","o","u"]]

print(consonant_words)




# long word

long=max([len(w) for w in text])

longest_word=[w for w in text if len(w)==long]

print(longest_word)


