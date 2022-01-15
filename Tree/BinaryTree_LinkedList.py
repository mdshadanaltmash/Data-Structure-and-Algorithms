import sys
sys.path.append('/Users/mdshadanaltmash/Algorithms/Queue')
from QueueUsingLinkedList import Queue

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
    #Root-> Left -> Right
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    #Left -> Root -> Right
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    # Left -> Right -> Root
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def searchBT(rootNode, node):
    if not rootNode:
        return "BT is Empty"
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.value.data == node:
            return "Found"
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)
    return "Not Found"

def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                print('Successfully Inserted')
                return
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                print('Successfully Inserted')
                return

def getDepeestNode(rootNode):
    if not rootNode:
        return("BT is Empty")
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)
    return (root.value)

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.value is dNode:
            root.value = None
            return
        if root.value.leftChild:
            if root.value.leftChild is dNode:
                root.value.leftChild = None
                return
            else:
                customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild:
            if root.value.rightChild is dNode:
                root.value.rightChild = None
                return
            else:
                customQueue.enqueue(root.value.rightChild)
    print("Deepest Node could not be deleted")

def deleteNode(rootNode, node):
    if not rootNode:
        return "BT is Empty"
    customQueue = Queue()
    customQueue.enqueue(rootNode)
    while not (customQueue.isEmpty()):
        root = customQueue.dequeue()
        if root.value.data == node:
            dNode = getDepeestNode(rootNode)
            root.value.data = dNode.data
            deleteDeepestNode(rootNode, dNode)
            return("Node is Deleted from Binary Tree")
        if root.value.leftChild is not None:
            customQueue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            customQueue.enqueue(root.value.rightChild)
    return("Node is not deleted or it is not present in BT")

def deleteBT(rootNode):
    if not rootNode:
        return "BT is Not Present"
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return("BT has been Successfully Deleted")
        

treeNode = TreeNode('Drinks')
hot = TreeNode('Hot')
cold = TreeNode('Cold')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
soda = TreeNode('Soda')
coke = TreeNode('Coke')
treeNode.leftChild = hot
treeNode.rightChild = cold
hot.leftChild = tea
hot.rightChild = coffee
cold.leftChild = soda
cold.rightChild = coke


# preOrderTraversal(treeNode)
# inOrderTraversal(treeNode)
# postOrderTraversal(treeNode)
insertNode(treeNode, TreeNode('Masala Tea'))
# deleteDeepestNode(treeNode, getDepeestNode(treeNode))
# levelOrderTraversal(treeNode)
print(deleteNode(treeNode, 'Cold'))
levelOrderTraversal(treeNode)
#print(searchBT(treeNode, 'Coke'))
print(deleteBT(treeNode))
levelOrderTraversal(treeNode)