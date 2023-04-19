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


# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
def inorder(root):
    if root:
        inorder(root.left)
        print(root.element)
        inorder(root.right)


""" An algorithm/method to re-arrange the order of a given sequence of integers so that when the
data items are inserted sequentially into an initially empty BST, the newly created BST will be
a balanced BST.
"""
def rearrange_sequence_for_bst_insertion(input_sequence):
        
    return


""" A method to insert a given sequence of integers into a Binary Search Tree data structure. This
method does not perform any sorting before insertion, simply inserting elements of the sequence
in the order provided.
"""
def create_balanced_bst(input_sequence):
    return


""" A method to demonstrate the tree shape of a Binary Search Tree data structure """
def print_bst_shape(input_bst):
    return


def main():
    sequence = [9, -1, 45, 6, 8, 21, 34, 5, 55, 65, 543, 18, 90, 122, 132, 0, 66, 100, -12, 17]
    
    # print(sequence)
    # sequence.sort()
    # print(sequence)

    r = TreeNode(50)
    for x in sequence:
        insert_into_bst(r, x)

    inorder(r)


main()
