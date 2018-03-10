import unittest
import q5

class TestQ5(unittest.TestCase):
    def test_common_case(self):
        # Run through all versions with the input.
        # Result should be same across all versions.
        change_to_make = 5
        coins = [1, 2, 3, 4]
        expected_num_ways = 6
        self.assertEqual(expected_num_ways, q5.make_change_top_down(change_to_make, coins))
        self.assertEqual(expected_num_ways, q5.make_change_bottom_up_v1(change_to_make, coins))
        self.assertEqual(expected_num_ways, q5.make_change_bottom_up_v2(change_to_make, coins))
    
    def test_out_of_order_coins(self):
        change_to_make = 5
        coins = [4, 1, 3, 2]
        expected_num_ways = 6
        self.assertEqual(expected_num_ways, q5.make_change_top_down(change_to_make, coins))
        self.assertEqual(expected_num_ways, q5.make_change_bottom_up_v1(change_to_make, coins))
        self.assertEqual(expected_num_ways, q5.make_change_bottom_up_v2(change_to_make, coins))
    
    def test_change_zero(self):
        change_to_make = 0
        coins = [4, 1, 3, 2]
        expected_num_ways = 1
        self.assertEqual(expected_num_ways, q5.make_change_top_down(change_to_make, coins))
        self.assertEqual(expected_num_ways, q5.make_change_bottom_up_v1(change_to_make, coins))
        self.assertEqual(expected_num_ways, q5.make_change_bottom_up_v2(change_to_make, coins))


if __name__ == "__main__":
    unittest.main()