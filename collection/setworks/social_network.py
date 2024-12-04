

users=["rahul","rohit","kohil","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohil","rishab","rahul"]

sanju_followers=["rohit","kohil","sanju"]



# follow_suggestions ["sanju","pandya","siraj"]

rahul_follow_suggestion=set(users).difference(set(rahul_followers))

print(rahul_follow_suggestion)



# mutal_friends of sanju and rahul

mutal_friends=set(rahul_followers).intersection (set(sanju_followers))

print(mutal_friends)





