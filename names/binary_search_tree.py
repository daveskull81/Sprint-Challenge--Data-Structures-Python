class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

        elif value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True

        if target > self.value:
            if self.right is not None:
                return self.right.contains(target)

        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)

        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()

        else:
            return self.value