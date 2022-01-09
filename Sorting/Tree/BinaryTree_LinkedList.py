class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def setLeftChild(self,leftChild):
        self.leftChild = leftChild
    def setRightChild(self, rightChild):
        self.rightChild = rightChild

treeNode = TreeNode('Drinks')
hot = TreeNode('Hot')
cold = TreeNode('Cold')
treeNode.leftChild = hot
treeNode.rightChild = cold
