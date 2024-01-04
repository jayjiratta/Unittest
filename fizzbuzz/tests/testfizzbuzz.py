from fizzbuzz.fizzbuzz_d import get_fizzbuzz
import unittest
class PrimeListTest(unittest.TestCase):
    def test_give_1_is_empty_str (self): 
        number = 1
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb,"")

    def test_give_9_is_fizz (self): 
        number = 9
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb,'Fizz') 

    def test_give_22_is_empty_str (self): 
        number = 22
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb,"") 

    def test_give_75_is_fizzbuzz (self): 
        number = 75
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb,"FizzBuzz") 

    def test_give_25_is_buzz (self): 
        number = 25
        are_fb = get_fizzbuzz(number)
        self.assertEqual(are_fb,"Buzz")          

    