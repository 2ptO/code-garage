import unittest
import q23

class TestQ23(unittest.TestCase):
    def test_list_with_cycles(self):
        # 1->2->3->4->2
        node1 = q23.LinkedListNode(1)
        node2 = q23.LinkedListNode(2)
        node3 = q23.LinkedListNode(3)
        # Linking node4 with node2
        node1.next_node = node2
        node2.next_node = node3
        node3.next_node = q23.LinkedListNode(4, node2)
        self.assertTrue(q23.contains_cycle(node1))
    
    def test_list_with_no_cycles(self):
        # 1->2->3->4-X
        node1 = q23.LinkedListNode(1)
        node1.next_node = q23.LinkedListNode(2, q23.LinkedListNode(3, q23.LinkedListNode(4)))
        t = node1
        while (t is not None):
            print(t.value)
            t = t.next_node
        self.assertFalse(q23.contains_cycle(node1))
    
    def test_list_with_single_node(self):
        node1 = q23.LinkedListNode(1)
        self.assertFalse(q23.contains_cycle(node1))
    
    def test_empty_list(self):
        self.assertFalse(q23.contains_cycle(None))

        


