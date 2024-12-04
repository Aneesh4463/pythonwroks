#palindrome

text=input("enter the text => ") #madam

reversed_text=text[::-1]

print("palindrome" if text==reversed_text else "not palindrome")
