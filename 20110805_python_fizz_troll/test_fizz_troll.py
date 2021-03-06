import unittest
from fizz_troll import fizz_buzz, fizz_alt, fizz_tern, fizz_dict, fizz_bit, fizz_func, fizz_matriz, fizz_gen, fizz_long

class TestFizzTroll(unittest.TestCase):

    functions = [fizz_buzz, fizz_alt, fizz_tern, fizz_dict, fizz_bit, fizz_func, fizz_matriz, fizz_gen, fizz_long]

    def assert_func(self, param, result, funcs = functions):
        for func in funcs:
            self.assertEqual(func(param), result)

    def test_fizzbuzz_de_1_diz_1(self):
        self.assert_func(1, 1)
   
    def test_fizzbuzz_de_2_diz_2(self):
        self.assert_func(2, 2)
     
    def test_fizzbuzz_de_3_diz_fizz(self):
        self.assert_func(3, "fizz")

    def test_fizzbuzz_de_6_diz_fizz(self):
        self.assert_func(6, "fizz")

    def test_fizzbuzz_de_5_diz_buzz(self):
        self.assert_func(5, "buzz")
    
    def test_fizzbuzz_de_10_diz_buzz(self):
        self.assert_func(10, "buzz")

    def test_fizzbuzz_de_15_diz_fizzbuzz(self):
        self.assert_func(15, "fizzbuzz")

    def test_fizzbuzz_de_30_diz_fizzbuzz(self):
        self.assert_func(30, "fizzbuzz")


unittest.main()
        
