class TreeComparator:
    def compare(self, node1,node2):
        """ check the base case (node1 and node 2 may be the leaf node)
            node1 may be None or node2 may be None """
        if not node1 or not node2:
            return node1 == node2

        #compare the data
        if node1.data is not node2.data:
            return False

        #check all left and right subtrees (children) recursively
        return self.compare(node1.left_node, node2.left_node) and self.compare(node1.right_node, node2.right_node)
class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left_node = None
        self.right_node = None
        # useful when implementing the remove function
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        # we can access the root node exclusively
        self.root = None

    def insert(self, data):
        # this is the first node in the BST
        if not self.root:
            self.root = Node(data , None)
        # if root is not empty i.e. BST is not empty
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # if we have to go to the left subtree
        if data < node.data:
            if node.left_node:
                # the left node exists so we keep going
                self.insert_node(data, node.left_node)
            else:
                # when there is no left child so we create one
                node.left_node = Node(data, node)
        # if we have to go to the right subtree
        else:
            if node.right_node:
                # the right node exists so we keep going
                self.insert_node(data, node.right_node)
            else:
                # when there is no right child so we create one
                node.right_node = Node(data, node)

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)
        else:
            print('Tree is Empty!!')

    def remove_node(self, data, node):
        if node is None:
            return None
        # first we have to find the node we need to remove
        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            # we found the node we need to remove
            # there are 3 cases
            if node.left_node is None and node.right_node is None:
                #LEAF NODE CASE
                print(" Removing a leaf Node...%d" % node.data)
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                if parent is None:
                    self.root = None

                del node

            elif node.left_node is None and node.right_node is not None:
                print('Removing a node with single right child...%d' % node.data)
                parent = node.parent
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    elif parent.right_node == node:
                        parent.right_node = node.right_node
                else:
                    self.root = node.right_node

                node.right_node.parent = parent
                del node
            elif node.right_node is None and node.left_node is not None:
                print('Removing a node with single left child...%d' % node.data)
                parent = node.parent
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    elif parent.right_node == node:
                        parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node

            else:
                #REMOVING A NODE WITH 2 CHILD
                print('Removing node with two children....')
                predecessor = self.get_predecessor(node.left_node)
                #swap the node and predecessor
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node .right_node:
            return self.get_predecessor(node.right_node)
        return node

    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    def get_min_value(self, node):
        if node.left_node:
            return self.get_min_value(node.left_node)
        return node.data

    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    def get_max_value(self, node):
        if node.right_node:
            return self.get_max_value(node.right_node)
        return node.data

    def traverse(self):
        if self.root:
            self.traverse_inorder(self.root)

    def traverse_inorder(self, node):
        if node.left_node:
            self.traverse_inorder(node.left_node)
        print(node.data)
        if node.right_node:
            self.traverse_inorder(node.right_node)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(8)
    bst.insert(12)
    bst.insert(-5)
    bst.insert(44)
    bst.insert(22)
    bst.insert(-12)
    bst.insert(19)
    print('Max Value: ', bst.get_max())
    print('Min Value: ', bst.get_min())
    bst.remove(10)
    bst.remove(5)
    bst.remove(44)
    bst.traverse()


    bst1 = BinarySearchTree()
    bst2 = BinarySearchTree()
    bst1.insert(-5)
    bst1.insert(44)
    bst1.insert(22)
    bst1.insert(-12)
    bst1.insert(19)
    bst1.insert(12)

    bst2.insert(-5)
    bst2.insert(44)
    bst2.insert(22)
    bst2.insert(-12)
    bst2.insert(19)
    bst2.insert(12)
    comparator = TreeComparator()
    print(comparator.compare(bst1.root, bst2.root))















