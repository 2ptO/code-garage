import unittest
import q24

class TestQ24(unittest.TestCase):
    def test_single_node_reversal(self):
        node1 = q24.LinkedListNode(1)
        self.assertEqual(q24.reverse_list(node1), node1)
    
    def test_two_node_reversal(self):
        node1 = q24.LinkedListNode(1)
        node2 = q24.LinkedListNode(2)
        # 2->1
        node2.next_node = node1
        self.assertEqual(q24.reverse_list(node2), node1)
    
    def test_multi_node_reversal(self):
        node1 = q24.LinkedListNode(1)
        node2 = q24.LinkedListNode(2)
        node3 = q24.LinkedListNode(3)
        node4 = q24.LinkedListNode(4)
        node5 = q24.LinkedListNode(5)
        node6 = q24.LinkedListNode(6)

        # 1->2->3->4->5->6
        node1.next_node = node2
        node2.next_node = node3
        node3.next_node = node4
        node4.next_node = node5
        node5.next_node = node6

        head = node1
        tail = node6

        # Collect the original list to be compared after reverse-in-place
        original_list = [x for x in q24.walk_list(head)]

        # assert head of the reversed list matches the
        # tail of the original list
        self.assertEqual(q24.reverse_list(head), tail)

        # In addtion to the head, make sure whole list is reversed
        reversed_list = [x for x in q24.walk_list(tail)]
       
        for i in range(len(original_list)):
            self.assertEqual(original_list[i], reversed_list[len(original_list)-1-i])