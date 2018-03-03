import unittest
import q2

class TestQ2(unittest.TestCase):
    def test_positive_nums(self):
        inputs = [7, 5, 4, 2, 6]
        expectedResult = 210
        actualResult = q2.get_highest_product_of_three(inputs)
        self.assertEqual(expectedResult, actualResult, "Invalid highest product of 3")
    
    def test_negative_nums(self):
        inputs = [7, 5, -4, 2, -6]
        expectedResult = 168
        actualResult = q2.get_highest_product_of_three(inputs)
        self.assertEqual(expectedResult, actualResult,
                        "expected:{} actual:{}".format(expectedResult, actualResult))
    
    def test_small_input_list_raises_error(self):
        inputs = [1]
        with self.assertRaises(ValueError):
            q2.get_highest_product_of_three(inputs)
        

if __name__ == "__main__":
    unittest.main()