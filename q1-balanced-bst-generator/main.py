sequence = [9, -1, 45, 6, 8, 21, 34, 5, 55, 65, 543, 18, 90, 122, 132, 0, 66, 100, -12, 17]


def create_balanced_bst(input_sequence):
    print("Demonstrating tree shape of BST:")


def demonstrate_bst_shape(input_sequence):
    print("Integer sequence before BST insertion:")
    print(input_sequence)

    print("Inserting sequence into BST...")
    create_balanced_bst(input_sequence)
    print("Demonstrating tree shape of BST:")


def main():
    demonstrate_bst_shape(sequence)


main()
