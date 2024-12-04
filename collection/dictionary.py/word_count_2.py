# word count        out=> {this:3,is:2 ...etc}

#step1: split text as words


text=" this is a simple program this program count the word count this program is simple"

text_count=text.split()

word_count={}

for w in text_count:

    if w in word_count:

        word_count[w]+=1

    else:

        word_count[w]=1

print(word_count)


