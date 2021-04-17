# binary search on reverse Array
arr=[11,10,9,8,7,6,5,4,3,2,1]
start=0
end=len(arr)-1
value=4
for i in range(end+1):
    mid=int(start+(end-start)/2)
    if arr[mid]==value:
        print("the",value,"is present @",mid,"position.")
        break
    elif value<arr[mid]:
        start=mid+1
    else:
        end=mid-1
