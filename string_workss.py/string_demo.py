# capitalize()          => 1st letter upperkeys & balnce all lowerkeys | eg:"helloPYTHON123"=> Hellopython123

# casefold()            => all key convert to lowerkeys | eg: "helloPYTHON123" => hellopython123

# isalpha()             => check alpha | output= true \ false | eg: "helloPYTHON123" => False |bcz no: involed

# isdigit()             => check digit | output= true \ false  | eg:"helloPYTHON123" => fasle | bcz alpha involve

# isalnum()             => check alpha & num  | output= true or false | eg: "helloPYTHON123" => true

# startswith(str)       => check word start at specified str | output= true \ false 

# endswith(str)         => check word end at specified str | output= true \ false 

# split()               => split the string | eg: helo,word =>  split(",")

# strip()               => remove leftend and rightend | only modified new text not modify oldtext

#lstrip()               => remove from leftend         | only modified new text not modify oldtext

#rstrip()               => remove from rightend        | only modified new text not modify oldtext

# replace("replaceword","whichone","ethraenam") => changes to anotherone

#string[start,end,step] => 

# index(" ")            => know the index of the word





# text="hello python"

# for ch in text:

#     print(ch)

# text="helloPYTHON123"

# result=text.capitalize()

# print(result)

# print(text.casefold())

# print(text.isdigit())

# print(text.isalpha())

# print(text.isalnum())

# print(text.startswith("he"))

# print(text.endswith("on"))




# textt="python,java,ruby"                          #split

# word=textt.split(",")

# print(word)



# test="\n this is a line \t"                     #remove \n,\t

# new_test=test.strip("\n,\t")            

# print(new_test)




# text2="helo world program"                          # o change two a

# new_text2=text2.replace("o","a",3)

# print(new_text2)


test3="hello python programing"                      #slicing
#      01234567890123456789
#   string_object[start,end,step]

print(test3[0:6:1])             #hello 
print(test3[:6:1])              #hello 
print(test3[0::1])              #hello python programing
print(test3[::2])               #hlopto rgaig
print(test3[6:15:1])            #python pr


string="hello"                                       #hello => reversed

reversed_text=string[::-1]

print(reversed_text)



test4="hello"                                       # index of text eg: o
#      01234
#text4.index("o")=>4

print(test4.index("o"))



