import unittest
import q28

class TestQ28(unittest.TestCase):
    def test_text_with_matching_paranthesis(self):
        text = "Sometimes (when I nest them (my parentheticals) "
        text += "too much (like this (and this))) they get confusing."
        open_paranthesis_pos = 10
        matching_paranthesis_pos = 79
        self.assertEqual(q28.find_matching_parenthesis(text, open_paranthesis_pos),
                         matching_paranthesis_pos)
    
    def test_text_with_no_matching_paranthesis(self):
        text = "a2 + (b2 (c2 + d2) + (e2 + f2)"
        open_paranthesis_pos = 5
        self.assertEqual(q28.find_matching_parenthesis(text, open_paranthesis_pos), -1)
    
    def test_invalid_args(self):
        with self.assertRaises(ValueError):
            text = "a2 + (b2 (c2 + d2) + (e2 + f2)"
            q28.find_matching_parenthesis(text, -1)
        with self.assertRaises(ValueError):
            text = "a2 + (b2 (c2 + d2) + (e2 + f2)"
            q28.find_matching_parenthesis(text, 133)

if __name__ == "__main__":
    unittest.main()

