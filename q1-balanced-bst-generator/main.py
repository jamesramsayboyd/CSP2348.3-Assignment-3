"""
James Boyd 10629572
CSP2348 Data Structures, Semester 1 2023
Assignment 3, Question 1
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
    def inorder(self):
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


def main():
    sequence = [9, -1, 45, 6, 8, 21, 34, 5, 55, 65, 543, 18, 90, 122, 132, 0, 66, 100, -12, 17]

    print("Sequence 1:")
    print(sequence)
    sorted_sequence = sort_for_bst_insertion(sequence)
    print("Sequence 1 (sorted for BST insertion):")
    print(sorted_sequence)
    print("Sequence 1 inserted into Binary Search Tree:")
    tree = BinaryTree()

    for i in sorted_sequence:
        tree.insert(i)

    print("Sequence 1 inserted into Binary Search Tree:")
    print_binary_tree_structure(tree.get_root())

    print()
    print("Sequence 2:")
    sequence_2 = generate_random_integer_set(20)
    print(sequence_2)
    sorted_sequence_2 = sort_for_bst_insertion(sequence_2)
    print("Sequence 2 (sorted for BST insertion):")
    print(sorted_sequence_2)
    tree.clear()

    for i in sorted_sequence_2:
        tree.insert(i)

    print("Sequence 1 inserted into Binary Search Tree:")
    print_binary_tree_structure(tree.get_root())


main()
