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
# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
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
#
#
# # https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.element)
#         inorder(root.right)
#
#
# def print_space(n, removed):
#     for i in range(n):
#         print("\t", end="")
#     if removed is None:
#         print(" ", end="")
#     else:
#         print(removed.element, end="")
#
#
# def height_of_tree(root):
#     if root is None:
#         return 0
#     return 1 + max(height_of_tree(root.left), height_of_tree(root.right))
#
#
# def print_binary_tree(root):
#     tree_level = []
#     temp = []
#     tree_level.append(root)
#     counter = 0
#     height = height_of_tree(root) - 1
#     number_of_elements = 2 ** (height + 1) - 1
#     while counter <= height:
#         removed = tree_level.pop(0)
#         if len(temp) == 0:
#             print_space(int(number_of_elements / (2 ** (counter + 1))), removed)
#         else:
#             print_space(int(number_of_elements / (2 ** counter)), removed)
#         if removed is None:
#             temp.append(None)
#             temp.append(None)
#         else:
#             temp.append(removed.left)
#             temp.append(removed.right)
#         if len(tree_level) == 0:
#             print("\n")
#             tree_level = temp
#             temp = []
#             counter += 1
#
#
# """ An algorithm/method to re-arrange the order of a given sequence of integers so that when the
# data items are inserted sequentially into an initially empty BST, the newly created BST will be
# a balanced BST.
# """
# def rearrange_sequence_for_bst_insertion(input_sequence):
#
#     return
#
#
# """ A method to insert a given sequence of integers into a Binary Search Tree data structure. This
# method does not perform any sorting before insertion, simply inserting elements of the sequence
# in the order provided.
# """
# def create_balanced_bst(input_sequence):
#     return
#
#
# """ A method to demonstrate the tree shape of a Binary Search Tree data structure """
# def print_bst_shape(input_bst):
#     return
#
#
def main():
    sequence = [9, -1, 45, 6, 8, 21, 34, 5, 55, 65, 543, 18, 90, 122, 132, 0, 66, 100, -12, 17]

    # print(sequence)
    # sequence.sort()
    # print(sequence)

    binary_tree = BinaryTree()
    for i in sequence:
        binary_tree.root = TreeNode(i)
        binary_tree.size += 1
        print("Element: ", TreeNode(i).element)
        print("Node no. ", binary_tree.size)
        print()

main()

# class Treenode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# class Tree:
#     def __init__(self):
#         self.root = None
#
#
# def height(root):
#     if root is None:
#         return 0
#     return max(height(root.left), height(root.right)) + 1
#
#
# def getcol(h):
#     if h == 1:
#         return 1
#     return getcol(h - 1) + getcol(h - 1) + 1
#
#
# def printTree(M, root, col, row, height):
#     if root is None:
#         return
#     M[row][col] = root.data
#     printTree(M, root.left, col - pow(2, height - 2), row + 1, height - 1)
#     printTree(M, root.right, col + pow(2, height - 2), row + 1, height - 1)
#
#
# def TreePrinter():
#     h = height(myTree.root)
#     col = getcol(h)
#     M = [[0 for _ in range(col)] for __ in range(h)]
#     printTree(M, myTree.root, col // 2, 0, h)
#     for i in M:
#         for j in i:
#             if j == 0:
#                 print(" ", end=" ")
#             else:
#                 print(j, end=" ")
#         print("")
#
#
# myTree = Tree()
# myTree.root = Treenode(1)
# myTree.root.left = Treenode(2)
# myTree.root.right = Treenode(3)
# myTree.root.left.left = Treenode(4)
# myTree.root.left.right = Treenode(5)
# myTree.root.right.left = Treenode(6)
# myTree.root.right.right = Treenode(7)
# TreePrinter()