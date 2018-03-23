import unittest
import q25

class TestQ25(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(q25.kth_to_last_node(None, 4))
    
    def test_single_node_list(self):
        node1 = q25.LinkedListNode(1)
        self.assertIsNone(q25.kth_to_last_node(node1, 1))
        self.assertEqual(q25.kth_to_last_node(node1, 0), node1)
    
    def test_valid_kth_node_from_last(self):
        # e.g. list 1-2-3-4
        node4 = q25.LinkedListNode(4)
        node3 = q25.LinkedListNode(3, node4)
        node2 = q25.LinkedListNode(2, node3)
        node1 = q25.LinkedListNode(1, node2)
        self.assertEqual(q25.kth_to_last_node(node1, 2), node2)
        self.assertEqual(q25.kth_to_last_node(node1, 0), node4)
        self.assertEqual(q25.kth_to_last_node(node1, 3), node1)
    
    def test_invalid_kth_node_from_last(self):
        node4 = q25.LinkedListNode(4)
        node3 = q25.LinkedListNode(3, node4)
        node2 = q25.LinkedListNode(2, node3)
        node1 = q25.LinkedListNode(1, node2)
        self.assertIsNone(q25.kth_to_last_node(node1, 12))
        self.assertIsNone(q25.kth_to_last_node(node1, 1234))

    def test_negative_kth_node_from_last(self):
        node4 = q25.LinkedListNode(4)
        node3 = q25.LinkedListNode(3, node4)
        node2 = q25.LinkedListNode(2, node3)
        node1 = q25.LinkedListNode(1, node2)
        with self.assertRaises(ValueError):
            q25.kth_to_last_node(node1, -4)

if __name__ == "__main__":
    unittest.main()
