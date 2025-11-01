from iterator import PowerOfTwoIterator

class PowerOfTwoIterable:
    def __init__(self, max_exponent):
        self.max_exponent = max_exponent

    def __iter__(self):
        # this function returns a new iterator every time
        return PowerOfTwoIterator(self.max_exponent)
