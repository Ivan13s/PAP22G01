import unittest
from test_th import is_prime, primes


class TestIsPrimeFunction(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(7), True)

    def test_is_not_prime(self):
        self.assertFalse(is_prime(4), False)

    def test_is_less_than_two(self):
        self.assertTrue(is_prime(1), False)

    # def test_limit_outside_1(self):
    #     self.assertTrue(primes(0), False)
    # def test_limit_not_int(self):
    #     self.assertRaises(TypeError, primes, 2.0001)
    def test_is_list(self):
        self.assertEqual(primes(10), [1, 2, 3, 5, 7])


if __name__ == "__main__":
    unittest.main()