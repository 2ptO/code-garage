import unittest
import q6

class TestQ6(unittest.TestCase):
    def test_partial_overlap(self):
        rect1 = {
            "x" : 2,
            "y" : 5,
            "width": 6,
            "height": 4
        }
        rect2 = {
            "x" : 4,
            "y" : 8,
            "width": 4,
            "height": 4
        }
        expected_overlap_rect = {
            "x" : 4,
            "y" : 8,
            "width": 4,
            "height": 1
        }
        actual_overlap_rect = q6.find_overlapping_rectangle(rect1, rect2)
        self.assertDictEqual(expected_overlap_rect, actual_overlap_rect)
    
    def test_full_overlapping_rectangles(self):
        outer = {
            "x" : 2,
            "y" : 2,
            "width": 6,
            "height": 6
        }
        inner = {
            "x" : 4,
            "y" : 4,
            "width": 2,
            "height": 3
        }
        self.assertDictEqual(inner, q6.find_overlapping_rectangle(outer, inner))
    
    def test_no_overlapping_rectangles(self):
        rect1 = {
            "x" : 2,
            "y" : 5,
            "width": 6,
            "height": 4
        }
        rect2 = {
            "x" : -4,
            "y" : -8,
            "width": 4,
            "height": 4
        }
        self.assertDictEqual({}, q6.find_overlapping_rectangle(rect1, rect2))

    def test_rectangles_bordering_but_no_overlap(self):
        rect1 = {
            "x" : 2,
            "y" : 6,
            "width": 6,
            "height": 4
        }
        rect2 = {
            "x" : 8,
            "y" : 6,
            "width": 4,
            "height": 4
        }
        self.assertDictEqual({}, q6.find_overlapping_rectangle(rect1, rect2))

