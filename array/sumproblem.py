arr=[1,2,3,4,5,6,7,8,2]
user=11
for i in range(len(arr)):
    
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==user:
            print(arr[i],arr[j])
            

print("-----------------------------------------------------------------")

arr=[1,2,3,4,5,6,7,8,9,11]
user=12
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==user:
            print(arr[i],arr[j])         