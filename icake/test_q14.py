import unittest
import q14

class TestQ14(unittest.TestCase):
    def test_matching_lengths(self):
        flight_time = 120
        movie_lengths = [45, 40, 80, 100, 60, 90]
        self.assertTrue(q14.is_movie_time_matching_flight_time(flight_time, movie_lengths))
    
    def test_no_matching_lengths(self):
        flight_time = 120
        movie_lengths = [45, 40, 100, 60, 90]
        self.assertFalse(q14.is_movie_time_matching_flight_time(flight_time, movie_lengths))

    def test_matching_lengths_with_duplicates(self):
        flight_time = 120
        movie_lengths = [45, 40, 100, 60, 90, 60]
        self.assertTrue(q14.is_movie_time_matching_flight_time(flight_time, movie_lengths))
    
    def test_no_matching_lenghts_with_invalid_times(self):
        flight_time = 120
        movie_lengths = [45, 40, 100, 0, 90, 60]
        self.assertFalse(q14.is_movie_time_matching_flight_time(flight_time, movie_lengths))

        movie_lengths = [45, 40, 140, -20, 90, 60]
        with self.assertRaises(ValueError):
            q14.is_movie_time_matching_flight_time(flight_time, movie_lengths)