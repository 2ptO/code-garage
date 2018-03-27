import unittest
import random
import q32


class TestQ32(unittest.TestCase):
    def test_sorted_scores(self):
        scores = [random.randint(0, 100) for _ in range(50)]
        self.assertListEqual(sorted(scores, reverse=True), q32.sort_scores(scores))
    