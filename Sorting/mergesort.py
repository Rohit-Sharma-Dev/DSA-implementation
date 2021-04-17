# def mergesort(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
#         r=arr[mid:]
#         l=arr[:mid]

#         mergesort(l)

#         mergesort(r)
#         i=j=k=0

#         while i<len(l) and j<len(r):
#             if l[i]<r[j]:
#                 arr[k]=l[i]
#                 i+=1
#             else:
#                 arr[k]=r[j]
#                 j+=1
#             k+=1

#         while  i<len(l):
#             arr[k]=l[i]
#             i+=1
#             k+=1

#         while j<len(r):
#             arr[k]=r[j]
#             j+=1
#             k+=1
#     return arr
# print(mergesort([12, 11, 13, 5, 6, 7]))

# if __name__=='__main__':
#     arr=[12, 11, 13, 5, 6, 7]
#     mergesort(arr)
#     print(arr)



arr = [1,2,3,5]
sum1 = sum(arr)
n = max(arr)
total_sum = (n(n+1))/2
missing_no = total_sum - sum1
print(missing_no)