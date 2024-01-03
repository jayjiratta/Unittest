from fizzbuzz.fizzbuzzcode.fizzbuzz_d import FizzBuzz
import unittest
class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3 (self):
        numbers = [1, 2, 3]
        are_fb = FizzBuzz(numbers)
        self.assertTrue(are_fb)
    