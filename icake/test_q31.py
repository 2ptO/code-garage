import unittest
import q31

class TestQ31(unittest.TestCase):
    def test_permutations(self):
        test_texts = []
        test_texts.append(("", 0))
        test_texts.append(("a", 1))
        test_texts.append(("ab", 2))
        test_texts.append(("abc", 6))
        test_texts.append(("abcd", 24))
        test_texts.append(("abcde", 120))
        test_texts.append(("abcdef", 720))
        for text, num_of_permutations_of_text in test_texts:
            self.assertEqual(num_of_permutations_of_text,
                            len(q31.permutations(text)))
        
        perm_of_abc = set(["abc",
                            "acb",
                            "bca",
                            "bac",
                            "cab",
                            "cba"]
                        )
        self.assertSetEqual(perm_of_abc, q31.permutations("abc"))
        
        