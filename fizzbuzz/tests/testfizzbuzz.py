from fizzbuzz.fizzbuzzcode.fizzbuzz_d import FizzBuzz
import unittest
class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        FB_list = [1, 2, 3]
        is_FB = FizzBuzz(FB_list)
        self.assertTrue(is_FB)