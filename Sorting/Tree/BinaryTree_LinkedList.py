class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def setLeftChild(self,leftChild):
        self.leftChild = leftChild
    def setRightChild(self, rightChild):
        self.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
treeNode = TreeNode('Drinks')
hot = TreeNode('Hot')
cold = TreeNode('Cold')
treeNode.leftChild = hot
treeNode.rightChild = cold

preOrderTraversal(treeNode)
inOrderTraversal(treeNode)