class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def iterative(root):
    if root :
        arr=[]
        brr=[]
        arr.append(root)
        while (len(arr)>0):
            node=arr.pop()
            # print(node.data,end=" ")
            brr.append(node.data)

            if node.right is not None:
                arr.append(node.right)
            if node .left is not None:
                arr.append(node.left)
    print(brr)


def iterativeinorder(root):
    arr=[]
    brr=[]
    while True:
        if root is not None :
            arr.append(root)
            root=root.left
        elif (arr):
            root=arr.pop()
            brr.append(root.data)
            # print(root.data ,end=" ")
            root=root.right
        else:
            break
            
    print(brr)



root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)
iterative(root )

iterativeinorder(root)
