a  = "abbc"
b = "accb"
c = 0
for i in a:
    for j in b:
        if i ==j:
            c+=1

if c==len(a):
    print("anagram :)")
else:
    print("not")


