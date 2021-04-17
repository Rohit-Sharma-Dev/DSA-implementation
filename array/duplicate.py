# finding duplicate in an unsorted array


arr=[3 ,1 ,2 ,5 ,3,7,1,3,3] 
b=[]
for i in range(len(arr)):
   for j in range(i+1,len(arr)):
       if arr[i]==arr[j]:
           if arr[j] not in b:
               b.append(arr[j])
               break

print(b)


# finding duplicate in sorted array

arr=[1,2,3,4,4,4,4,5,6,7,8,9,10,11,11]
b=[]
for i in range(1,len(arr)):
    if arr[i-1]==arr[i]:
        if arr[i] not in b:
            b.append(arr[i])
            continue
print(b)

