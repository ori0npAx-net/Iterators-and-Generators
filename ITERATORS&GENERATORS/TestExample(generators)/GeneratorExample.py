class FactorDemo:
        """Showcases modern generator behavior in Python 3.8+"""
        def __init__(self, n):
            self.n = n
# -------------------------------
# Case 1: Return with value (legal now, but silent)
# -------------------------------
        def bad_generator_mix(self):
            for k in range(1, self.n + 1):
                if self.n % k == 0:
                    if k > 10:
                        return "Too big!" # Allowed, but ends generator silently
                    yield k

# -------------------------------
# Case 2: Logical Error (still compiles but wrong)
# -------------------------------
        def bad_generator_logic(self):
            results = []
            for k in range(1, self.n + 1):  
                if self.n % k == 0:
                    results.append(k)
                    yield results #yields growing list snapshot instead of one factor

# -------------------------------
# Case 3: Correct Generator
# -------------------------------
        def good_generator(self):
            for k in range(1, self.n + 1):
                if self.n % k == 0:
                    yield k



