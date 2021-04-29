class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data

    def PrintTree(self):
        print(self.data)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.right=Node(4)
root.left.left=Node(5)
root.right.left=Node(7)
root.right.right=Node(8)

root.left.PrintTree()



