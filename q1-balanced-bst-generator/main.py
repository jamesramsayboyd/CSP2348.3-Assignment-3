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



#
#
# # https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# def print_in_order_traversal(root):
#     if root:
#         print_in_order_traversal(root.left)
#         print(root.element, end="")
#         print_in_order_traversal(root.right)


def sort_array_for_bst_insertion(arr):
    if not arr:
        return None  # base case for recursive algorithm

    arr.sort()  # Sort array in ascending order first
    midpoint = (len(arr)) // 2  # Find middle element of array
    root = TreeNode(arr[midpoint])  # Middle element instantiated as root node of BST

    root.left = sort_array_for_bst_insertion(arr[:midpoint])
    root.right = sort_array_for_bst_insertion(arr[midpoint + 1:])
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


def main():
    sequence = [9, -1, 45, 6, 8, 21, 34, 5, 55, 65, 543, 18, 90, 122, 132, 0, 66, 100, -12, 17]
    sequence_2 = []

    print("First sequence of numbers, unsorted:")
    for i in sequence:
        print(i, end="  ")
    print()
    print()
    root = sort_array_for_bst_insertion(sequence)
    print("First sequence of numbers, sorted for BST insertion:")
    print_pre_order(root)
    print("Binary search tree shape:")



main()
