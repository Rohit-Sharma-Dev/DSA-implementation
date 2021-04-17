arr=[1,2,3,4,5,6,7,8,9,11,13]
for i in range(1,max(arr)+1):
    if i not in arr:
        print(i,"this no. is not found")

# if the no. of element is from 1 to n

arr=[1,2,3,4,5,6,7,8,9,10,12]
for i in range(1,len(arr)+1):
    if i not in arr:
        print(i,"not in array")


# 2nd approach
arr=[1,2,3,4,5,6,7,8,9,10,12]
n=len(arr)
sum_arr=sum(arr)
sum_arrn=n*n+3*n+3
sum_arrn=sum_arrn//2
mising_no= sum_arrn-sum_arr

print(mising_no,"this is the misiing no.")


