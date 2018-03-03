import unittest
import q1

class TestQ1(unittest.TestCase):
    def test_boundary_conditions(self):
        inputs = []
        results = q1.get_products_of_all_ints_except_at_index(inputs)
        self.assertEqual(inputs, results, "Invalid result for empty inputs")

        inputs.append(1)
        results = q1.get_products_of_all_ints_except_at_index(inputs)
        self.assertListEqual(inputs, results, "Invalid result for single number")
    
    def test_natural_numbers(self):
        inputs = [3,4,5,7,1]
        expected = [140, 105, 84, 60, 420]
        actual = q1.get_products_of_all_ints_except_at_index(inputs)
        self.assertListEqual(expected, actual, "Invalid products")
    
    def test_inputs_with_zero(self):
        inputs = [3,4,0,7,1]
        expected = [0, 0, 84, 0, 0]
        actual = q1.get_products_of_all_ints_except_at_index(inputs)
        self.assertListEqual(expected, actual, "Invalid products")    
    
if __name__ == "__main__":
    unittest.main()