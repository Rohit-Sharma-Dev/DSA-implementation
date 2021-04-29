# all order in type in sigle escan 

class Node :
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val,end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


def levelorder(root):
    q=[root]
    while len(q)>0:
        node=q.pop(0)
        print(node.val,end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

def leafnode(root):
    if root:
        if not root.left and not root.right:
            print(root.val,end=" ")
        levelorder(root.left)
        levelorder(root.right)


def height(root):
    if root is None:
        return 0 
 
    else :
 
        # Compute the depth of each subtree
        depth_left = height(root.left)
        depth_right= height(root.right)
 
        # Use the larger one
        if (depth_left> depth_right):
            return depth_left+1
        else:
            return depth_right+1



def traversal(root):
    print("in order :")
    inorder(root)
    print(end=" ")

    print("postorder :")
    postorder(root)
    print(end=" ")

    print("levelorder :")
    levelorder(root)
    print(end=" ")

    print("preorder :")
    preorder(root )
    print(end=" ")


    print ("Height of tree is %d" %(height(root)))


    # print(height(root))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
traversal(root)



# diameter of btree

# def dia(node):
#     if not node:
#         return 0 ,0
#     lp,lw=dia(node.left)
#     rp,rw=dia(node.right)
    
#     return 1+max(lp,rp),max(lw,rw,1+rp+lp)

# class Node:
#     def diameterOfBinaryTree(self, root) :
#         return dia(root)[1]-1

# # root=[1,2,3,4,5]

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# print(diameterOfBinaryTree(root))



# # Are you happy with your current progress?
# # Do you think you are winning?
# # Where are you at in the journey?
# # Pawan Gnana Raj11:13 AM
# # Any challenges you are facing?
# # Your SMART goal in DSA and communication



    