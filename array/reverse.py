# reverse the array
arr=[3,98,90,91,97,56,65]
for i in range(len(arr)//2):
    arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
print(arr)


# 2nd approach
arr=[3,98,90,91,97,56,65]
arr1=[]
for i in range(len(arr)):
    arr1.append(arr[len(arr)-1-i])
print(arr1)

# 3rd approach

arr=[3,98,90,91,97,56,65]
print(arr[::-1])

