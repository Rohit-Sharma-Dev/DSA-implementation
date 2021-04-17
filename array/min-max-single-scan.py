arr=[64, 34, 25, 12, 22, 11, 90]
b=arr[1]
c=arr[1]
for i in range(len(arr)):
    if b>arr[i]:
        b=arr[i]
    elif c<arr[i]:
        c=arr[i]

print(b,c)


print("-----------------------------------------------------------------")
# 2nd approach 
arr=[64, 34, 25, 12, 22, 11, 90]
for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr[0],arr[-1])