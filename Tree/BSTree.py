from Queue.QueueUsingLinkedList import Queue
class TreeNode:
    def __init__(self, data, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right
    
def insertNode( rootNode, newNode):
    if rootNode.data is None:
        rootNode.data = newNode
    elif newNode<=rootNode.data:
        if rootNode.left is None:
            rootNode.left = TreeNode(newNode)
        else:
            insertNode(rootNode.left, newNode)
    else:
        if rootNode.right is None:
            rootNode.right = TreeNode(newNode)
        else:
            insertNode(rootNode.right, newNode)
    return ('Node inserted Successfully')

def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)
def preOrderTraversal_list(rootNode, nodes=[]):
    if rootNode is None:
        return
    nodes.append(rootNode.data)
    preOrderTraversal_list(rootNode.left, nodes)
    preOrderTraversal_list(rootNode.right, nodes)
    return (nodes)

def inOrderTraversal_list(rootNode, nodes=[]):
    if rootNode is None:
        return
    inOrderTraversal_list(rootNode.left, nodes)
    nodes.append(rootNode.data)
    inOrderTraversal_list(rootNode.right, nodes)
    return (nodes)

def postOrderTraversal_list(rootNode, nodes=[]):
    if rootNode is None:
        return
    postOrderTraversal_list(rootNode.left, nodes)
    postOrderTraversal_list(rootNode.right, nodes)
    nodes.append(rootNode.data)
    return (nodes)

newBst = TreeNode(None)
print(insertNode(newBst, 70))
print(insertNode(newBst, 60))
print(insertNode(newBst, 80))
print(insertNode(newBst, 90))
print(insertNode(newBst, 10))
print(insertNode(newBst, 50))
print(insertNode(newBst, 40))
print(insertNode(newBst, 100))
# preOrderTraversal(newBst)
print(preOrderTraversal_list(newBst))
print(inOrderTraversal_list(newBst))
print(postOrderTraversal_list(newBst))