# Write a class TempTracker with these methods:

# insert() - records a new temperature
# get_max() - returns the highest temp we've seen so far
# get_min() - returns the lowest temp we've seen so far
# get_mean() - returns the mean of all temps we've seen so far
# get_mode() - returns a mode of all temps we've seen so far
# Optimize for space and time. Favor speeding up the getter methods 
# get_max(), get_min(), get_mean(), and get_mode() over speeding up the insert() method.

# get_mean() should return a float, but the rest of the getter methods can return integers. 
# Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, 
# so we can assume they'll all be in the range 0..1100..110.

# If there is more than one mode, return any of the modes.

import random

class TempTracker:
    MIN_TEMP = 0
    MAX_TEMP = 110
    def __init__(self):
        self.temps = [0 for x in range(TempTracker.MAX_TEMP+1)]
        self.min = TempTracker.MAX_TEMP
        self.max = TempTracker.MIN_TEMP

        # Calculate mean
        self.sum = 0
        self.num_of_entries = 0
        self.mean = 0

        # Calculate mode
        self.max_occurence = 0
        self.mode = 0
    
    def insert(self, temp):
        # boundary check
        if temp < TempTracker.MIN_TEMP or temp > TempTracker.MAX_TEMP:
            raise ValueError("Temperature should be range of 0 to 110 Farenheit")
        
        self.temps[temp] += 1
        
        if temp > self.max:
            self.max = temp
        if temp < self.min:
            self.min = temp
        
        self.sum += temp
        self.num_of_entries += 1
        self.mean = self.sum / self.num_of_entries
        if self.temps[temp] > self.max_occurence:
            self.max_occurence = self.temps[temp]
            self.mode = temp

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min
    
    def get_mean(self):
        return self.mean
    
    def get_mode(self):
        return self.mode
    
    def __str__(self):
        temps_in_string = ""
        for temp, frequency in enumerate(self.temps):
            temps_in_string += "Temp: {} Freq: {}\n".format(temp, frequency)
        return temps_in_string