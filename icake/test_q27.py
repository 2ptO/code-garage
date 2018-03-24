import unittest
import q27

class TestQ27(unittest.TestCase):
    def test_reverse_even_words_in_sentence(self):
        sentence = list("jumps fox brown quick")
        q27.reverse_words(sentence)
        self.assertEqual(sentence, list("quick brown fox jumps"))
    
    def test_reverse_odd_words_in_sentence(self):
        sentence = list("fox brown quick")
        q27.reverse_words(sentence)
        self.assertEqual(sentence, list("quick brown fox"))

if __name__ == "__main__":
    unittest.main()
        
