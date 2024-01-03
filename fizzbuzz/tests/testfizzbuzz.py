from fizzbuzz.fizzbuzzcode.fizzbuzz_d import FizzBuzz
import unittest
class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3 (self):
        numbers = [1, 2, 3]
        are_fb = FizzBuzz(numbers)
        self.assertTrue(are_fb)

    def test_give_9 (self):
        numbers = [9]
        are_fb = FizzBuzz(numbers)
        self.assertTrue(are_fb) 

    def test_give_22_26_28 (self):
        numbers = [22, 26, 28]
        are_fb = FizzBuzz(numbers)
        self.assertTrue(are_fb) 

    def test_give_75_79_54 (self):
        numbers = [75, 79, 54]
        are_fb = FizzBuzz(numbers)
        self.assertTrue(are_fb) 

    def test_give_69_96_1024_51_113 (self):
        numbers = [69, 96, 1024, 51, 113]
        are_fb = FizzBuzz(numbers)
        self.assertTrue(are_fb)          

    