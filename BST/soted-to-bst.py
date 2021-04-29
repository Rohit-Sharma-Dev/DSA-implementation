# ------------------ Convert Sorted Array to Binary Search Tree

class Node :
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def sortedArrayToBST(self,nums) :
    n=len(nums)
    if n==0:
        return None
    return nums[n//2],self.sortedArrayToBST(nums[:n//2]),self.sortedArrayToBST(nums[(n//2)+1:])


# sortedArrayToBST([2,3,4,5,6,7,8])
