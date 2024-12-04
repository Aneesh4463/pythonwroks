#print pangram or not 

text="The quick brown for jumps over the lazy dog"

text=text.casefold()

alphabet=("abcdefghijklmnopqrstuvwxyz")

is_pangram=False

for ch  in alphabet:

    if ch not in text:

        is_pangram=True

        break
    
print(is_pangram)
