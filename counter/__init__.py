# counter/__init__.py

import numpy as np

class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1
        return self.value

    def decrement(self):
        self.value -= 1
        return self.value

    def reset(self):
        self.value = 0
        return self.value

    def randomize(self, low=0, high=100):
        """Set counter to a random integer between `low` and `high`."""
        self.value = np.random.randint(low, high)
        return self.value
