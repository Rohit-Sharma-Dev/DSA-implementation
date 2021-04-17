def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr.pop()
    elements_greter=[]
    elements_smaller=[]
    for i in arr:
        if i > pivot:
            elements_greter.append(i)
        else:
            elements_smaller.append(i)
    return quick_sort(elements_smaller)+[pivot]+quick_sort(elements_greter)

print(quick_sort([3,4,53,2,4,2,2,3,34,13,5,56,90,77,88,9998,22]))