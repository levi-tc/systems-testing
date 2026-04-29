from node import Node


class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
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
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        """Recursive helper for find.

        Args:
            data (int): data to find
            node (Node): current node in the recursion

        Returns:
            Node: matching node, or None if not found
        """
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """Detach the entire tree by clearing the root reference."""
        self.root = None

    def printTree(self):
        """Print the tree using an in-order traversal."""
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """In-order traversal: left, root, right.

        Args:
            node (Node): subtree root to traverse
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """Pre-order traversal: root, left, right.

        Args:
            node (Node): subtree root to traverse
        """
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        """Post-order traversal: left, right, root.

        Args:
            node (Node): subtree root to traverse
        """
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')
