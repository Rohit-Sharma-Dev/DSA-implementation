arr = [64, 34, 25, 12, 22, 11, 90]
# for i in range(len(arr)):
#     min_idx=i
#     for j in range(i+1,len(arr)):
#         if arr[min_idx]>arr[j]:
#             min_idx=j
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]
# print(arr)



for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)


