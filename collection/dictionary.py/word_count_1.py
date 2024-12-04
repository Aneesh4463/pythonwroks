#word count
#iterate words
#chk w exist in wordcount
# add w as key in wordcount and value as 1

words=["hello","hi","hello","hi","hello","this","is","this","is","hello"]

word_count={}

# for w in words:

#     if w in word_count:

#         word_count[w]+=1

#     else:

#         word_count[w]=1

# print(word_count)


#another method


word_frequency={ w:words.count(w)  for w in words }


print(word_frequency)


recursive_words=[ k  for k,v in word_frequency.items()  if v>1 ]


print(recursive_words)



#display non_recursive_words

