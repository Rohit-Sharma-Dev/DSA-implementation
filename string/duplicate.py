a = "abcdadc"
b = ""
for i in range(1,len(a)):
    if a[i-1] in a[i:]:
        if a[i-1] not in b:
            b+=a[i-1]
if len(b)!= 0:
    print(b)