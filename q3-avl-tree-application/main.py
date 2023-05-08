class Node:
    def __init__(self, e):
        self.element = e
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return self.height == 0

    def leaf_node_sorter(self, bool):
        if self.node is None:
            return []

        nodes = []

        l = self.node.left.leaf_node_sorter(bool)
        for i in l:
            nodes.append(i)

        if self.is_leaf() is bool:
            nodes.append(self.node.element)

        l = self.node.right.leaf_node_sorter(bool)
        for i in l:
            nodes.append(i)

        return nodes

    def insert(self, key):
        tree = self.node

        new_node = Node(key)

        if tree is None:
            self.node = new_node
            self.node.left = AVLTree()
            self.node.right = AVLTree()

        elif key < tree.element:
            self.node.left.insert(key)

        elif key > tree.element:
            self.node.right.insert(key)

        else:
            print("ERROR: Node", key, "already exists in AVL Tree!")

        self.rebalance()

    def rebalance(self):
        '''
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.l_rotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.r_rotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.r_rotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.l_rotate()
                self.update_heights()
                self.update_balances()

    def r_rotate(self):
        # Rotate left pivoting on self
        #debug('Rotating ' + str(self.node.key) + ' right')
        a = self.node
        b = self.node.left.node
        t = b.right.node

        self.node = b
        b.right.node = a
        a.left.node = t

    def l_rotate(self):
        # Rotate left pivoting on self
        #debug('Rotating ' + str(self.node.key) + ' left')
        a = self.node
        b = self.node.right.node
        t = b.left.node

        self.node = b
        b.left.node = a
        a.right.node = t

    def update_heights(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def logical_predecessor(self, node):
        '''
        Find the biggest valued node in LEFT child
        '''
        node = node.left.node
        if node is not None:
            while node.right is not None:
                if node.right.node is None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        '''
        Find the smallest valued node in RIGHT child
        '''
        node = node.right.node
        if node is not None:  # just a sanity check

            while node.left is not None:
                #debug("LS: traversing: " + str(node.key))
                if node.left.node is None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self is None or self.node is None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return (abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced()

    def in_order_traverse(self):
        if self.node is None:
            return []

        inlist = []
        l = self.node.left.in_order_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.element)

        l = self.node.right.in_order_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    """ Q3(b) A method to return the pre-order traversal sequence of the AVL tree """
    def pre_order_traverse(self):
        if self.node is None:
            return []

        inlist = []
        inlist.append(self.node.element)

        l = self.node.left.pre_order_traverse()
        for i in l:
            inlist.append(i)

        l = self.node.right.pre_order_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    """ Q3(b) A method to return the post-order traversal sequence of the AVL tree """
    def post_order_traverse(self):
        if self.node is None:
            return []

        inlist = []
        l = self.node.left.post_order_traverse()
        for i in l:
            inlist.append(i)

        l = self.node.right.post_order_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.element)

        return inlist

    def display(self, level=0, pref=''):
        self.update_heights()  # Must update heights before balances
        self.update_balances()
        if self.node is not None:
            if self.node.left is not None:
                self.node.right.display(level + 2, '>')
            print(' ' * level * 2, pref, self.node.element, "[" + str(self.height) + ":" + str(self.balance) + "]",
                  'L' if self.is_leaf() else ' ')
            if self.node.left is not None:
                self.node.left.display(level + 2, '<')

    def get_root(self):
        return self.node

    def delete_node(self, tree, key):
        root = tree.node

        if root is None:
            return

        elif key < root.element:
            self.delete_node(root.left, key)

        elif key > root.element:
            self.delete_node(root.right, key)

        else:  # key is found
            if root.right.node is None:  # Node has left child but no right child
                temp_node = root.left.node
                root.node = None
                return temp_node
            elif root.left.node is None:  # Node has right child but no left child
                temp_node = root.right.node
                root.node = None
                return temp_node

            temp_node = self.logical_predecessor(root.right.node)
            temp_node_child = temp_node.right
            if temp_node is not tree:
                temp_node.left = temp_node_child.right
            else:
                temp_node.right = temp_node_child.right

            tree.element = temp_node_child.element

            self.rebalance()
            return tree


""" Prompts the user to enter a valid input between minimum and maximum values
provided as arguments. Used for numbered choice menus (e.g. Press 1 to _____) and
entering elements of an array
"""
def take_only_valid_input(min_value, max_value):
    while True:
        user_input = input()
        if user_input.lstrip("-").isdigit():  # Allows for negative integer input
            user_input = int(user_input)
            if min_value < user_input < max_value:
                return user_input
        print("ERROR: Enter a valid integer between", min_value + 1, "and", max_value - 1)
        print()


""" A function to display level 2 of the console menu, allowing users to perform
several operations on the Binary Search Tree provided as a parameter
"""
def level_2_menu(tree):
    while True:
        print("1. Display the AVL tree, showing the height and balance factor for each node\n"
              "2. Print the pre-order, in-order and post-order traversal sequences of the AVL tree\n"
              "3. Print all leaf nodes of the AVL tree, and all non-leaf nodes (separately)\n"
              "4. Insert a new integer key into the AVL tree\n"
              "5. Delete an integer key from the AVL tree\n"
              "6. Return to initial menu\n")
        print("Enter choice:")
        user_input = take_only_valid_input(0, 9)
        if user_input == 1:  # Displays tree shape
            print("Displaying AVL Tree rotated 90 degrees anti-clockwise (root node is at far left)")
            tree.display()
            print("\n")
        elif user_input == 2:  # Displays various traversal sequences
            print("Displaying Pre-Order traversal sequence:")
            print(tree.pre_order_traverse())
            print("\nDisplaying In-Order traversal sequence:")
            print(tree.in_order_traverse())
            print("\nDisplaying Post-Order traversal sequence:")
            print(tree.post_order_traverse())
            print("\n")
        elif user_input == 3:  # Displays leaf/non-leaf nodes
            print("Displaying all leaf nodes of the AVL tree:")
            print(tree.leaf_node_sorter(True))
            print("Displaying all non-leaf nodes of the AVL tree:")
            print(tree.leaf_node_sorter(False))
            print("\n")
        elif user_input == 4:  # Adds an integer to the AVL Tree
            print("Enter an integer to add it to the BST:")
            add_node = take_only_valid_input(-1000, 1000)
            tree.insert(add_node)
            print("\n")
        elif user_input == 5:  # Deletes an integer from the BST
            print("Enter an integer to delete it from the BST:")
            delete_node = take_only_valid_input(-1000, 1000)
            #tree.delete(delete_node)
            tree.delete_node(tree, delete_node)
            print("\n")
        else:  # Returns to level 1 menu
            print()
            return


def main():
    sample_dataset = [58, 82, -55, 20, 35, 79, 23, 14, 0, -21, 103, 92, 44, 84, 50, 46, 47, 49, 45, 72, 89]

    while True:
        print("1. Pre-load a sequence of integers to build an AVL Tree\n"
              "2. Manually enter integer values, one by one, to build an AVL Tree\n"
              "3. Exit")
        print()
        print("Enter choice: ")
        user_choice = take_only_valid_input(0, 4)
        print()

        if user_choice == 1:
            print("Using sample dataset", sample_dataset)
            print()
            tree = AVLTree(sample_dataset)
            level_2_menu(tree)

        elif user_choice == 2:
            print("Enter size of tree: ")
            tree_size = take_only_valid_input(0, 30)
            tree = manually_create_bst(tree_size)
            level_2_menu(tree)

        elif user_choice == 3:
            print("Goodbye")
            break


main()
