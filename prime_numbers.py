# MODULES

import math
import unittest


# METHODS

# True if trial_division fails to find smaller composite numbers of n
def is_prime(n, verbose=False):
    if n == 1 or n == 0: return False
    if verbose: print(f"Checking {n} for primality...")
    if trial_division(n):
        return False    
    return True

# True if n is composed of smaller products between 2 and sqrt of n
def trial_division(n, verbose=False):
    i = 2
    sqrt_n = math.sqrt(n)
    if verbose: print(f"sqrt of {n} is {sqrt_n}")
    while i <= sqrt_n:
        if is_multiple_of(i, n):
            return True
        i += 1
    return False

# True if source is evenly divisible by x and x is not zero
def is_multiple_of(x, source, verbose=False):
    if x == 0:
        return False
    # Evenly divisible?
    if source % x == 0:
        if verbose: print(f"{x} is a multiple of {source}")
        return True
    else:
        if verbose: print(f"{x} is NOT a multiple of {source}")
        return False


# MAIN BODY

prime_candidates = [0,1,3,9,10,11,31,88,72,113]
print('================================')
print('Checking prime candidates... ')

for i in prime_candidates:
    print(f"{i} is prime: {is_prime(i)}")  
    print('')


# UNIT TESTING

class TestPrimeMethods(unittest.TestCase):

    def test_trial_division(self):
        self.assertTrue(trial_division(8))
        self.assertFalse(trial_division(7))

    def test_31_is_prime(self):
        self.assertTrue(is_prime(31))

    def test_2_is_multiple_of_10(self):
        self.assertTrue(is_multiple_of(2, 10))

    def test_3_not_multiple_of_10(self):
        self.assertFalse(is_multiple_of(3, 10))

    def test_is_multiple_false_for_divby0(self):
        self.assertFalse(is_multiple_of(0, 10))

    def test_1_is_not_prime(self):
        self.assertFalse(is_prime(1))

    def test_0_is_not_prime(self):
        self.assertFalse(is_prime(0))

if __name__ == '__main__':
    unittest.main()