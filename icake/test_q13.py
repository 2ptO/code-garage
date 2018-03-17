import unittest
import q13

class TestQ13(unittest.TestCase):
    def test_word_list_rotating_word_middle(self):
        words = [
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist',
            'asymptote',  # <-- rotates here!
            'babka',
            'banoffee',
            'engender',
            'karpatka',
            'othellolagkage'
        ]
        self.assertEqual(q13.find_rotation_point(words), 'asymptote',
                            "Rotating word is in the middle")

    def test_word_list_rotating_word_last(self):
        words = [
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist',
            'asymptote',  # <-- rotates here!
        ]
        self.assertEqual(q13.find_rotation_point(words), 'asymptote',
                    "Rotating word is the last word")
    
    def test_word_list_rotating_word_first_half(self):
        words = [
            'xenoepist',
            'asymptote',  # <-- rotates here!
            'babka',
            'banoffee',
            'engender',
            'karpatka',
            'othellolagkage'
        ]
        self.assertEqual(q13.find_rotation_point(words), 'asymptote',
                    "Rotating word is the last word")
    
    def test_word_list_no_rotating_word(self):
        words = [
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist'
        ]
        self.assertIsNone(q13.find_rotation_point(words))
    
    def test_empty_word_list(self):
        words = []
        self.assertIsNone(q13.find_rotation_point(words))
    
    def test_one_word_list(self):
        words = ["Hello"]
        self.assertEqual(q13.find_rotation_point(words), words[0])


        