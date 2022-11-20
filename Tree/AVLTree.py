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

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)
        else:
            print('Tree is Empty!!')

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

    def remove_node(self, data, node):
        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            # we Found the node which we have to delete
            # but there are 3 case in deleting the node
            if node.left_node is None and node.right_node is None:
                # CASE 1, LEAF NODE
                print(" Removing a leaf Node...%d" % node.data)
                parent = node.parent

                # check whether the node is left child of its parent or right child
                if parent is None:
                    self.root = None
                else:
                    if parent.left_node == node:
                        parent.left_node = None
                    elif parent.right_node == node:
                        parent.right_node = None
                del node

                self.handle_violations(parent)

            #CASE 2
            elif node.left_node is not None and node.right_node is None:
                # node with single left child
                print(' Removing a node with single left child... %d' % node.data)
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

                self.handle_violations(parent)

            elif node.right_node is not None and node.left_node is None:
                # node with single right child
                print(' Removing a node with single right child... %d' % node.data)
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

                self.handle_violations(parent)

            else:
                # CASE 3
                #REMOVING A NODE WITH 2 CHILD
                print('Removing node with two children....')
                predecessor = self.get_predecessor(node.left_node)
                predecessor.data, node.data = node.data, predecessor.data
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node .right_node:
            return self.get_predecessor(node.right_node)
        return node

