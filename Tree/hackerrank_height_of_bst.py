class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root is None:
            return -1
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

T=8
myTree=Solution()
root=None
datas = [3,5,2,1,4,6,7,8]
for data in datas:
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       