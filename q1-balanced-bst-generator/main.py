import random

# Source: CSP2348_M6_Binary Trees.pptx
class TreeNode:
    def __init__(self, e):
        self.element = e
        self.left = None
        self.right = None


# Source: CSP2348_M6_Binary Trees.pptx
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0


def sort_array_for_bst_insertion(arr):
    if not arr:
        return None  # base case for recursive algorithm

    arr.sort()  # Sort array in ascending order first
    midpoint = (len(arr)) // 2  # Find middle element of array
    root = TreeNode(arr[midpoint])  # Middle element instantiated as node of BST

    root.left = sort_array_for_bst_insertion(arr[:midpoint])  # Recursively find midpoint of left side of array
    root.right = sort_array_for_bst_insertion(arr[midpoint + 1:])  # # Recursively find midpoint of right side of array
    return root


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


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def get_col(h):
    if h == 1:
        return 1
    return get_col(h - 1) + get_col(h - 1) + 1


def print_tree(m, root, col, row, tree_height):
    if root is None:
        return
    m[row][col] = root.element
    print_tree(m, root.left, col - pow(2, tree_height - 2), row + 1, tree_height - 1)
    print_tree(m, root.right, col + pow(2, tree_height - 2), row + 1, tree_height - 1)


def tree_printer(tree):
    h = height(tree.root)
    col = get_col(h)
    m = [[0 for _ in range(col)] for __ in range(h)]
    print_tree(m, tree.root, col // 2, 0, h)
    for i in m:
        for j in i:
            if j == 0:
                print(" ", end=" ")
            else:
                print(j, end=" ")
        print("")


""" Generates an array of random numbers between 0 and 99. Array size is chosen by the user. """
def generate_random_integer_set(a):
    array = []
    for i in range(a):
        array.append(random.randint(0, 99))
    return array


def print_spaces(n, node):
    for i in range(n):
        print("\t", end="")
    if node is None:
        print("  ", end="")
    else:
        print(node.element, end="")


def height_of_tree(node):
    if node is None:
        return 0
    return 1 + max(height_of_tree(node.left), height_of_tree(node.right))


# def print_binary_tree(node):
#     tree_level = []
#     temp = []
#     tree_level.append(node)
#     counter = 0
#     tree_height = height_of_tree(node) - 1
#     number_of_elements = 2 ** (tree_height + 1) - 1
#     while counter <= tree_height:
#         node = tree_level.pop(0)
#         if len(temp) == 0:
#             print_spaces(int(number_of_elements / (2 ** (counter + 1))), node)
#         else:
#             print_spaces(int(number_of_elements / (2 ** counter)), node)
#         if node is None:
#             temp.append(None)
#             temp.append(None)
#         else:
#             temp.append(node.left)
#             temp.append(node.right)
#         if len(tree_level) == 0:
#             print("\n")
#             tree_level = temp
#             temp = []
#             counter += 1

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
    sequence_2 = generate_random_integer_set(20)

    # print("First sequence of numbers, unsorted:")
    # for i in sequence:
    #     print(i, end="  ")
    # print()
    # root = sort_array_for_bst_insertion(sequence)
    # print("First sequence of numbers, sorted for BST insertion:")
    # print_pre_order(root)
    # print()
    # print("Binary search tree shape:")
    # print()
    #
    # print("Second sequence of numbers, unsorted:")
    # for i in sequence_2:
    #     print(i, end="  ")
    # print()
    # root = sort_array_for_bst_insertion(sequence_2)
    # print("First sequence of numbers, sorted for BST insertion:")
    # print_pre_order(root)
    # print()
    # print("Binary search tree shape:")
    # print()

    root = sort_array_for_bst_insertion(sequence)
    my_tree = BinaryTree()
    my_tree.root = root
    #tree_printer(my_tree)
    #print_binary_tree(root)

    root = sort_array_for_bst_insertion(sequence_2)
    my_tree = BinaryTree()
    my_tree.root = root
    #tree_printer(my_tree)
    #print_binary_tree(root)
    print_binary_tree_structure(root)


main()
