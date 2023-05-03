import random

# Source: CSP2348_M6_Binary Trees.pptx
class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None
        self.right = None

    def insert(self, element):
        if self.element:
            if element < self.element:
                if self.left is None:
                    self.left = TreeNode(element)
                else:
                    self.left.insert(element)
            elif element > self.element:
                if self.element is None:
                    self.right = TreeNode(element)
                else:
                    self.right.insert(element)
        else:
            self.element = element


# Source: CSP2348_M6_Binary Trees.pptx
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0


""" A recursive algorithm that sorts a given array of integers such that when the elements are
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


def sequential_bst_insert(root, element):
    if root.element is None:
        return TreeNode(element)
    else:
        if root.element is element:
            return root
        elif root.element < element:
            root.right = sequential_bst_insert(root.right, element)
        else:
            root.left = sequential_bst_insert(root.left, element)
    return root


""" A recursive algorithm that sorts a given array of integers such that when the elements are
inserted into an initially empty Binary Search Tree, the resulting BST will be balanced.
"""
def sort_array_for_bst_insertion(arr):
    if not arr:
        return None  # base case for recursive algorithm

    arr.sort()  # Sort array in ascending order first
    midpoint = (len(arr)) // 2  # Find middle element of array
    node = TreeNode(arr[midpoint])  # Middle element instantiated as node of BST

    node.left = sort_array_for_bst_insertion(arr[:midpoint])  # Recursively find midpoint of left side of array
    node.right = sort_array_for_bst_insertion(arr[midpoint + 1:])  # # Recursively find midpoint of right side of array
    return node


def print_pre_order(tree_node):
    if not tree_node:
        return

    print(tree_node.element, end="  ")
    print_pre_order(tree_node.left)
    print_pre_order(tree_node.right)


def insert_into_bst(root, e):
    if root is None:
        return TreeNode(e)
    else:
        if root.element is e:
            return root
        elif root.element < e:
            root.right = insert_into_bst(root.right, e)
        else:
            root.left = insert_into_bst(root.left, e)
    return root


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

# Source: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/72497198#72497198
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
    #sorted_arr = []
    #sequence_2 = generate_random_integer_set(20)

    print(sequence)
    sorted_sequence = sort_for_bst_insertion(sequence)
    print(sorted_sequence)
    root = TreeNode

    for i in sorted_sequence:
        root.insert(root, i)
    print_pre_order(root)

    # for i in sequence:
    #     insert_into_bst(root, i)
    #
    # #root = sort_array_for_bst_insertion(sequence)
    # print_pre_order(root)
    # #print_binary_tree_structure(root)

    # print("First sequence of numbers, unsorted:")
    # for i in sequence:
    #     print(i, end="  ")
    # print()
    # root = sort_array_for_bst_insertion(sequence)
    # print("First sequence of numbers, sorted for BST insertion:")
    # print_pre_order(root)
    # # print()
    # # print("Binary search tree shape:")
    # # print()
    # #
    # # print("Second sequence of numbers, unsorted:")
    # # for i in sequence_2:
    # #     print(i, end="  ")
    # # print()
    # # root = sort_array_for_bst_insertion(sequence_2)
    # # print("First sequence of numbers, sorted for BST insertion:")
    # # print_pre_order(root)
    # # print()
    # # print("Binary search tree shape:")
    # # print()
    #
    # root = sort_array_for_bst_insertion(sequence)
    # my_tree = BinaryTree()
    # my_tree.root = root
    # #tree_printer(my_tree)
    # #print_binary_tree(root)
    #
    # root = sort_array_for_bst_insertion(sequence_2)
    # my_tree = BinaryTree()
    # my_tree.root = root
    # #tree_printer(my_tree)
    # #print_binary_tree(root)
    # print_binary_tree_structure(root)


main()
