# check sorted or not

arr=[3,4,5,6,7,8,9,10,1,0]
for i in range(1,len(arr)):
    if arr[i-1]>arr[i]:
        print("no")
        break
else:
    print("yes")
    
    

