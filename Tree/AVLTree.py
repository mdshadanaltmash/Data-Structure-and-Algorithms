class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 0


class AVLTree:
    def __init__(self):
        # We can access the root node exclusively
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # confider left subtree
        if data < node.data:
            # we have to check whether left child is none or not
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data, node)
                node.height = max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1
            # confider right subtree
        else:
            # we have to check whether right child is none or not
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data, node)
                node.height = max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1
        self.balance_tree(node)

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)
        else:
            print('Tree is Empty!!')

    def remove_node(self, data, node):
        # Find node using BST logic because AVL tree is also a BST
        if data < node.data:
            self.remove_node(data, node.left)
        elif data > node.data:
            self.remove_node(data, node.right)
        else:
            # We found the node which we have to delete
            # CASE 1: when node is a leaf node
            if node.left is None and node.right is None:
                print('Removing node with 0 children: ', node.data)
                parent = node.parent

                if parent is None:
                    self.root = None
                else:
                    # checking whether node is a left child or right child
                    if parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None
                del node
                self.balance_tree(parent)

            # CASE 2: When node has a single child
            # Checking if it has single left child
            elif node.left and not node.right:
                print('Removing node with 1 left children: ', node.data)
                parent = node.parent

                if parent is None:
                    self.root = node.left
                else:
                    if parent.left == node:
                        parent.left = node.left
                    if parent.right == node:
                        parent.right = node.left

                node.left.parent = parent
                del node
                self.balance_tree(parent)

            # Checking if it has single right child
            elif not node.left and node.right:
                print('Removing node with 1 right children: ', node.data)
                parent = node.parent

                if parent is None:
                    self.root = node.right
                else:
                    if parent.left == node:
                        parent.left = node.right
                    if parent.right == node:
                        parent.right = node.right

                node.right.parent = parent
                del node
                self.balance_tree(parent)

            # CASE 3: When node has 2 child
            else:
                print('Removing node with 2 children')
                predecessor = self.get_predecessor(node.left)
                predecessor.data, node.data = node.data, predecessor.data
                self.remove_node(data, predecessor)

    def rotate_right(self, node):
        print('Rotating to the right on node: ', node.data)
        temp_left_node = node.left
        t = temp_left_node.right

        temp_left_node.right = node
        node.left = t

        if t is not None:
            t.parent = node

        temp_left_node.parent, node.parent = node.parent, temp_left_node

        if temp_left_node.parent and temp_left_node.parent.left == node:
            temp_left_node.parent.left = node
        if temp_left_node.parent and temp_left_node.parent.right == node:
            temp_left_node.parent.right = node

        if node == self.root:
            self.root = temp_left_node
        node.height = max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1
        temp_left_node.height = max(self.calculate_height(temp_left_node.left),
                                    self.calculate_height(temp_left_node.right)) + 1

    def rotate_left(self, node):
        print('Rotating to the left on node: ', node.data)
        temp_right_node = node.right
        t = temp_right_node.left

        temp_right_node.left = node
        node.right = t

        if t is not None:
            t.parent = node

        temp_right_node.parent, node.parent = node.parent, temp_right_node

        if temp_right_node.parent and temp_right_node.parent.left == node:
            temp_right_node.parent.left = node
        if temp_right_node.parent and temp_right_node.parent.right == node:
            temp_right_node.parent.right = node

        if node == self.root:
            self.root = temp_right_node
        node.height = max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1
        temp_right_node.height = max(self.calculate_height(temp_right_node.left),
                                     self.calculate_height(temp_right_node.right)) + 1

    @staticmethod
    def calculate_height(node):
        # when node is null
        if not node:
            return -1
        return node.height

    def calculate_balance(self, node):
        if not node:
            return 0
        return self.calculate_height(node.left) - self.calculate_height(node.right)

    def balance_helper(self, node):
        balance = self.calculate_balance(node)

        # when balance is >1 then it is a left heavy tree, but it can be left-left heavy or left-right heavy
        if balance > 1:
            # left-right heavy situation = left rotation on parent + right rotation on grandparent
            if self.calculate_balance(node.left) < 0:
                self.rotate_left(node.left)
            # this is a right rotation on grandparent.
            # If left-left heavy situation then single right rotation is required
            self.rotate_right(node)

        # when balance is <-1 then it is a right heavy tree, but it can be right-left heavy or right-right heavy
        elif balance < -1:
            # right-left heavy situation = right rotation on parent + left rotation on grandparent
            if self.calculate_balance(node.right) > 0:
                self.rotate_right(node.right)
            # this is a right rotation on grandparent.
            # If left-left heavy situation then single right rotation is required
            self.rotate_left(node)

    def balance_tree(self, node):
        # check the nodes from the node we have inserted/deleted up to the root node
        while node is not None:
            node.height = max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1
            self.balance_helper(node)
            # whenever we balance (rotations) then it may happen that it violates
            # AVL properties in other part of the tree, that is why we need to check till the root.
            node = node.parent

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        return node

    def traverse_in_order_from_root(self):
        self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left:
            self.traverse_in_order(node.left)

        if node.left:
            l = node.left.data
        else:
            l = 'Null'
        if node.right:
            r = node.right.data
        else:
            r = 'Null'
        if node.parent:
            p = node.parent.data
        else:
            p = 'Null'
        print(f"{node.data}'s left: {l} right: {r} parent: {p} height: {node.height}")

        if node.right:
            self.traverse_in_order(node.right)


if __name__ == '__main__':
    avl = AVLTree()
    avl.insert(5)
    avl.insert(3)
    avl.insert(10)
    avl.insert(2)
    avl.insert(4)
    avl.insert(15)
    avl.traverse_in_order_from_root()

    avl.remove(15)
    avl.remove(10)

