user=input()
b=""
for i in range(len(user)):
    b+=user[len(user)-1-i]
if b==user:
    print("palindrome")
else:
    print("not palindrome")