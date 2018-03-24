import unittest
import q29

class TestQ29(unittest.TestCase):
    def test_text_is_nested(self):
        text = "{ [ ] ( ) }"
        self.assertTrue(q29.is_nested(text))
    
    def test_text_is_not_nested(self):
        text1 = "{ [ ( ] ) }"
        text2 = "{ [ }"
        self.assertFalse(q29.is_nested(text1))
        self.assertFalse(q29.is_nested(text2))

if __name__ == "__main__":
    unittest.main()