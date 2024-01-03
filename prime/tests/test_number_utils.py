from prime.coe_number.number_utils import is_prime_list
import unittest
class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_mixed_primes_and_non_primes(self):
        prime_list = [1, 2, 4, 5]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_all_non_primes(self):
        prime_list = [4, 6, 8, 9]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_empty_list(self):
        prime_list = []
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)  # An empty list is considered prime by convention

    def test_large_prime(self):
        prime_list = [9999991]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
