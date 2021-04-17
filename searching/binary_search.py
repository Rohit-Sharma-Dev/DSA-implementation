# binary search 
arr=[1,2,3,4,5,6,7,8,9,12,15]
start=0
end=len(arr)-1

value=15
for i in range(start,end+1):
    mid=int(start+(end-start)/2)
    if arr[mid]==value:
        print("the",value,"is present @",mid,"position.")
        break
    elif value<arr[mid]:
        end=mid-1
    else:
        start=mid+1
