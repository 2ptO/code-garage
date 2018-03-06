import unittest
import q3

class TestQ3(unittest.TestCase):
    def test_empty_list_of_times(self):
        inputs = []
        self.assertListEqual(inputs,
                            q3.merge_ranges_optimized(inputs),
                            "Merged times is not empty")
    
    def test_presorted_meeting_times(self):
        meeting_times = [(1, 4), (4, 5), (6, 9), (8, 10), (11, 13)]
        expected_merged_times = [(1, 5), (6, 10), (11, 13)]
        self.assertListEqual(expected_merged_times,
                            q3.merge_ranges_optimized(meeting_times),
                            "merged meeting times differ")
    
    def test_unsorted_meeting_times(self):
        meeting_times = [(11, 13), (1, 4), (6, 9), (4, 5),  (8, 10)]
        expected_merged_times = [(1, 5), (6, 10), (11, 13)]
        self.assertListEqual(expected_merged_times,
                            q3.merge_ranges_optimized(meeting_times),
                            "merged meeting times differ")
        
        meeting_times = [(4, 6), (5, 8)]
        expected_merged_times = [(4, 8)]
        self.assertListEqual(expected_merged_times,
                            q3.merge_ranges_optimized(meeting_times),
                            "merged times don't match for two pairs")
        
    def test_unsorted_meeting_times_no_overlap(self):
        meeting_times = [(1, 3), (7, 9), (5, 6)]
        expected_merged_times = sorted(meeting_times)
        self.assertListEqual(expected_merged_times,
                            q3.merge_ranges_optimized(meeting_times),
                            "merged times don't match for no overlapping timings")
        
if __name__ == "__main__":
    unittest.main()
