import unittest
from random import randint
from statistics import mean, mode, StatisticsError
import q7

class TestQ7(unittest.TestCase):
    def test_random_temps(self):
        num_temps = 50
        test_temps = [randint(q7.TempTracker.MIN_TEMP, q7.TempTracker.MAX_TEMP) \
                        for x in range(num_temps)]
        test_temp_tracker = q7.TempTracker()
        for temp in test_temps:
            test_temp_tracker.insert(temp)
        self.assertEqual(max(test_temps), test_temp_tracker.get_max())
        self.assertEqual(min(test_temps), test_temp_tracker.get_min())
        self.assertEqual(mean(test_temps), test_temp_tracker.get_mean())
        try:
            self.assertEqual(mode(test_temps), test_temp_tracker.get_mode())
        except(StatisticsError):
            # If random inputs generate more than one mode in the list,
            # statistics.mode will raise a error. Ignore it for test purposes.
            pass

    def test_invalid_temps(self):
        test_temp_tracker = q7.TempTracker()
        with self.assertRaises(ValueError):
            test_temp_tracker.insert(-1)
        with self.assertRaises(ValueError):
            test_temp_tracker.insert(120)
