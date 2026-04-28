from node import Node

class Tree:
    """ Tree class for binary tree structure. """

    def __init__(self):
        """ Constructor for Tree class. Initializes root as None. """
        self.root = None

    def getRoot(self):
        """ 
        Method to get the root of the tree.
        @return Node: The root node of the tree.
        """
        return self.root

    def add(self, data):
        """ 
        Method to add data to the tree. If root is empty, creates root.
        @param data: The value to be added to the tree.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """
        Helper method to recursively find the correct position for new data.
        @param data: Data to add.
        @param node: Current node being evaluated.
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """
        Method to find a specific value in the tree.
        @param data: The value to search for.
        @return Node: The node containing the data, or None if not found.
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        """
        Recursive helper for the find method.
        @param data: Value to find.
        @param node: Current node in recursion.
        """
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)
        return None

    def deleteTree(self):
        """ Resets the tree by setting the root to None. """
        self.root = None

    def printTree(self):
        """ Prints the tree using Inorder traversal (Left, Root, Right). """
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ', end='')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """
        Prints the tree in Preorder (Root, Left, Right).
        @param node: Current node.
        """
        if node is not None:
            print(str(node.data) + ' ', end='')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        """
        Prints the tree in Postorder (Left, Right, Root).
        @param node: Current node.
        """
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ', end='')