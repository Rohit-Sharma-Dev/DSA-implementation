a  = "listen"
b = "silent"
c = 0
for i in range(len(a)):
    if a[i] in b:
        c+=1
if len(b) == len(a) == c:
    print("anagram")