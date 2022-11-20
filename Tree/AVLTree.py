class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            # we have to check the left node is None
            if node.left_node:
                # when the left child is not none
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                node.height = max(self.get_height(node.left_node), self.get_height(node.right_node))+1
        else:
            # we have to check the right node is None
            if node.right_node:
                # when the right child is not none
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                node.height = max(self.get_height(node.left_node), self.get_height(node.right_node))+1

        # after every insertion we have to check whether the AVL Properties are violated
        self.handle_violations(node)

