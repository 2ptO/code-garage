import unittest
import q11

class TestQ1(unittest.TestCase):
    def test_some_url(self):
        urls = [
            "https://github.com/torvalds/linux/tree/master/kernel",
            "https://github.com/github/linux",
            "https://git-scm.com/download/linux",
            "https://cloud.google.com/bigquery/public-data/github",
            "https://www.google.com",

        ]
        linux_on_github = "https://github.com/github/linux"
        url_tracker = q11.Trie()
        
        for url in urls:
            self.assertTrue(url_tracker.add_url(url))

        self.assertFalse(url_tracker.add_url(linux_on_github))
            