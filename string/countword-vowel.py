# for checking its length i have also written the code in this file

user=input("enter your word for :-")
count_vowel=0
count=0
for i in user :
    if i in "aeiouAEIOu":
        count_vowel+=1
        count+=1
    else:
        count+=1

print("the length of the given string is :-",len(user))
print("no. of vowel in your word is :-",count_vowel)
print("no. of word in your word is:- ",count)


# for finding length #approch 2

count=0
for i in range(len(user)):
    count+=1

print("the lentgh of the user is",count)
