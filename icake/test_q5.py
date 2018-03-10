import unittest
import q5

class TestQ5(unittest.TestCase):
    def test_common_case(self):
        # Run through all versions with the input.
        # Result should be same across all versions.
        change_to_make = 4
        coins = [1, 2, 3]
        expected_num_ways = 4
        actual_num_ways = q5.make_change_top_down(change_to_make, coins)
        self.assertEqual(expected_num_ways, actual_num_ways)


if __name__ == "__main__":
    unittest.main()