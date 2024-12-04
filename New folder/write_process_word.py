
words_path="C:\\Users\\User\\Desktop\\pythonworksss\\collection\\file\\words.txt"

palindrome_path="C:\\Users\\User\\Desktop\\pythonworksss\\collection\\file\\palindrome.txt"


is_words=open(words_path,"r")

is_palindrome=open(palindrome_path,"w")



for words in is_words:

    words=words.rstrip("\n")

    reversed_word=words[::-1]

    if reversed_word==words:

        is_palindrome.write(words+"\n")




is_palindrome.close()

is_words.close()








