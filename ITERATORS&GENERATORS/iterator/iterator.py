import time
class PowerOfTwoIterator:
    def __init__(self, max_exponent):
        self.max_exponent = max_exponent
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_exponent:
            result = 2 ** self.current
            self.current += 1
            time.sleep(0.5)
            return result
        else:
            raise StopIteration
        
    def reset(self):
        self.current=0
        
