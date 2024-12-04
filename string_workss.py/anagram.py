# input source_word="silent"  heart
#       target_word="listen" earth

source_code="earth"

target_code="heart"

is_anagram=True

for ch in target_code:

    if ch not in source_code:

        is_anagram=False

print(is_anagram)