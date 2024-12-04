#input=>  text="hellopython"
# out=>   llehopython

text="hellopython"

index=text.index("o")

rev_hello=text[index-1::-1]

bal=text[index::]

result=rev_hello+bal

print(result)









