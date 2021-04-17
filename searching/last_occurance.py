arr=[1,2,3,4,5,5,5,6,7,8,9,12,15]
start=0
end=len(arr)-1
res=0
value=5
for i in range(start,end+1):
    mid=int(start+(end-start)/2)
    if arr[mid]==value:
        res=mid
        start=mid+1
    elif value<arr[mid]:
        end=mid-1
    else:
        start=mid+1
print("the last occurance of ",value,"is at",res,"position.")
#          