# #  Search in a Binary Search Tree

# class solution(object):
#     def searchBst(self,root,val):
#         if not root:
#             return None
#         v=root.val
#         if v==val:
#              print(root)
#         elif v>val:
#             print(self.searchBst(root.left,val))
#         print(self.searchBst(root.right,val))

# # soluti




# #---------- Validate Binary Search Tree


# def check(root,l, r):
#     if not root:
#         return True
#     v=root.val
#     return v>l and v<r and check(root.left,l,v) and check (root.right,v,r)


# class Solution:
#     def isValidBST(self, root) :
#         inf=2<<31+1
#         return check(root,-inf,inf)



# inserting in a TreeNode


class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def insert(node, key):
 
    # If the tree is empty,
    # return a new node
    if not node :
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print(inorder(root))


