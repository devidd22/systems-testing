import unittest
from tree import Tree

class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        for val in [3, 4, 0, 8, 2]:
            self.tree.add(val)

    def test_find_existing_element(self):
        """ Test that an existing element is found correctly. """
        node = self.tree.find(8)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 8)

    def test_find_non_existing_element(self):
        """ Test that searching for a missing element returns None. """
        node = self.tree.find(100)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()