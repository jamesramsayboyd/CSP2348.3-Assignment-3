"""
James Boyd 10629572
CSP2348 Data Structures, Semester 1 2023
Assignment 3, Question 2
"""

import random

""" A class representing a Binary Search Tree, implementing several methods
for traversing the structure, inserting/searching/deleting nodes
"""
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree
    def search(self, e):
        current = self.root  # Start from the root

        while current is not None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:  # element matches current.element
                return True  # Element is found

        return False

    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root is None:
            self.root = self.create_new_node(e)  # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current is not None:
                if e < current.element:
                    parent = current
                    current = current.left
                elif e > current.element:
                    parent = current
                    current = current.right
                else:
                    return False  # Duplicate node? not inserted

            # Create the new node and attach it to the parent node
            if e < parent.element:
                parent.left = self.create_new_node(e)
            else:
                parent.right = self.create_new_node(e)

        self.size += 1  # Increase tree size
        return True  # Element inserted

    # Create a new TreeNode for element e
    def create_new_node(self, e):
        return TreeNode(e)

    # Return the size of the tree
    def get_size(self):
        return self.size

    # Inorder traversal from the root
    def in_order(self):
        self.in_order_helper(self.root)

    # Inorder traversal from a subtree
    def in_order_helper(self, r):
        if r is not None:
            self.in_order_helper(r.left)
            print(r.element, end=" ")
            self.in_order_helper(r.right)

    # Postorder traversal from the root
    def post_order(self):
        self.post_order_helper(self.root)

    # Postorder traversal from a subtree
    def post_order_helper(self, root):
        if root is not None:
            self.post_order_helper(root.left)
            self.post_order_helper(root.right)
            print(root.element, end=" ")

    # Preorder traversal from the root
    def pre_order(self):
        self.pre_order_helper(self.root)

    # Preorder traversal from a subtree
    def pre_order_helper(self, root):
        if root is not None:
            print(root.element, end=" ")
            self.pre_order_helper(root.left)
            self.pre_order_helper(root.right)

    # Return true if the tree is empty
    def is_empty(self):
        return self.size == 0

    # Remove all elements from the tree
    def clear(self):
        self.root = None
        self.size = 0

    # Return the root of the tree
    def get_root(self):
        return self.root

    """ Q2 a) The Inverse In-Order traversal algorithm """
    def inverse_in_order(self):
        self.inverse_in_order_helper(self.root)

    def inverse_in_order_helper(self, r):
        if r is not None:
            self.inverse_in_order_helper(r.right)
            print(r.element, end=" ")
            self.inverse_in_order_helper(r.left)

    """ Q2 b) A function to print all leaf nodes of the BST """
    def leaf_bst(self):
        self.leaf_bst_helper(self.root)

    def leaf_bst_helper(self, r):
        if r is not None:
            self.leaf_bst_helper(r.left)
            if (r.left is None) and (r.right is None):
                print(r.element, end=" ")
            self.leaf_bst_helper(r.right)

    """ Q2 b) A function to print all non-leaf nodes of the BST """
    def non_leaf_bst(self):
        self.non_leaf_bst_helper(self.root)

    def non_leaf_bst_helper(self, r):
        if r is not None:
            self.non_leaf_bst_helper(r.left)
            if (r.left is not None) or (r.right is not None):
                print(r.element, end=" ")
            self.non_leaf_bst_helper(r.right)

    """ Q3 c) A function that, for a given node N in a BST, counts the total number
    of nodes of the sub-tree rooted at N, and prints all nodes (including N) of 
    the subtree
    """
    def total_nodes_bst(self, n):
        return

    """ Q3 d) A function that calculates the depth of a given node N in a BST """
    def depth_node_bst(self, n):
        return

    """ Q3 e) A function that calculates the depth of a subtree rooted at a given
    node N in a BST
    """
    def subtree_bst(self, n):
        return

    """ Q3 f) A function that deletes a node from a BST """
    def delete_node(self, key):
        return


""" A class representing a node of a Binary Search Tree """
class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None  # Point to the right node, default None


""" Q1: Balanced BST Generation
A recursive algorithm that sorts a given array of integers such that when the elements are
inserted into an initially empty Binary Search Tree, the resulting BST will be balanced. Returns
a newly sorted array.
"""
def sort_for_bst_insertion(array):
    sorted_arr = []

    def sort(arr):
        if len(arr) == 0:
            return

        arr.sort()
        mid = (len(arr)) // 2
        sorted_arr.append(arr[mid])

        sort(arr[0:mid])
        sort(arr[mid + 1:])
        return sorted_arr

    return sort(array)


""" Generates an array of random numbers between 0 and 99. Array size is chosen by the user. """
def generate_random_integer_set(a):
    array = []
    for i in range(a):
        array.append(random.randint(0, 99))
    return array


def height_of_tree(node):
    if node is None:
        return 0
    return 1 + max(height_of_tree(node.left), height_of_tree(node.right))


""" A method to print the tree-shaped structure of a binary search tree
Source: Mera, A. (2022, Jun 4). print binary tree level by level in python. StackOverflow
     https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/72497198#72497198
"""
def print_binary_tree_structure(root):

    number_of_levels = height_of_tree(root)
    width = pow(2, number_of_levels + 1)

    q = [(root, 0, width, 'c')]
    levels = []

    while (q):
        node, level, x, align = q.pop(0)
        if node:
            if len(levels) <= level:
                levels.append([])

            levels[level].append([node, level, x, align])
            seg = width // (pow(2, level + 1))
            q.append((node.left, level + 1, x - seg, 'l'))
            q.append((node.right, level + 1, x + seg, 'r'))

    for i, l in enumerate(levels):
        pre = 0
        preline = 0
        linestr = ''
        pstr = ''
        seg = width // (pow(2, i + 1))
        for n in l:
            valstr = str(n[0].element)
            if n[3] == 'r':
                linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                preline = n[2]
            if n[3] == 'l':
                linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)
                preline = n[2] + seg + seg // 2
            pstr += ' ' * (n[2] - pre - len(valstr)) + valstr  # correct the position according to the number size
            pre = n[2]
        print(linestr)
        print(pstr)


""" Prompts the user to enter a valid input, i.e. an integer between 0 and the highest numbered choice
featured within the numbered choice menu (provided as an argument)
"""
def take_only_valid_input(max_value):
    while True:
        user_input = input("Enter choice: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if 0 < user_input < max_value:
                return user_input
        print("ERROR: Enter a valid integer between 1 and", max_value - 1)
        print()


def main():
    sequence = [58, 84, 68, 23, 38, 82, 26, 17, 24, 106, 95, 48, 88, 54, 50, 51, 53, 49, -6, -46]
    tree = BinaryTree()
    for i in sequence:
        tree.insert(i)

    print_binary_tree_structure(tree.get_root())

    #tree.in_order()
    print()
    #tree.inverse_in_order()
    print("In order traversal: ")
    tree.in_order()
    print("\nOnly leaf nodes:")
    tree.leaf_bst()
    print("\nOnly non-leaf nodes:")
    tree.non_leaf_bst()


    # while True:
    #     print("1. Pre-load a sequence of integers to build a BST\n"
    #           "2. Manually enter integer values, one by one, to build a BST\n"
    #           "3. Exit")
    #     print()
    #     user_choice = take_only_valid_input(4)
    #     print()
    #
    #     if user_choice == 1:
    #         print("1. Display the tree shape of current BST, and then show the pre-order, in-order,"
    #               " post-order and inverse-in-order traversal sequences of the BST\n"
    #               "2. Show all leaf nodes of the BST, and all non-leaf nodes (separately)\n"
    #               "3. Show a sub-tree and count its nodes\n"
    #               "4. Show the depth of a given node in the BST\n"
    #               "5. Show the depth of a subtree of the BST\n"
    #               "6. Insert a new integer key into the bST\n"
    #               "7. Delete an integer key from the BST\n"
    #               "8. Exit")
    #         user_choice = take_only_valid_input(9)
    #     elif user_choice == 2:
    #         print("Enter value: ")
    #     elif user_choice == 3:
    #         print("Goodbye")
    #         break


main()
