import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tree import Tree


class TestFind(unittest.TestCase):
    """Unit tests for Tree._find."""

    def setUp(self):
        self.tree = Tree()
        for value in (3, 4, 0, 8, 2):
            self.tree.add(value)

    def test_find_existing_value_returns_node_with_data(self):
        node = self.tree._find(8, self.tree.getRoot())
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 8)

    def test_find_root_value(self):
        node = self.tree._find(3, self.tree.getRoot())
        self.assertIs(node, self.tree.getRoot())

    def test_find_missing_value_returns_none(self):
        node = self.tree._find(99, self.tree.getRoot())
        self.assertIsNone(node)

    def test_find_via_public_wrapper(self):
        self.assertEqual(self.tree.find(2).data, 2)
        self.assertIsNone(self.tree.find(42))


if __name__ == '__main__':
    unittest.main()
