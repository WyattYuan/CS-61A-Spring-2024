import unittest
from cs61a.week1.somefunction import factorial, fibonacci, is_palindrome, count_words, is_prime
from doctest import testmod, run_docstring_examples

# assert factorial(0) == 2, "Test case 1 fucked up"
run_docstring_examples(factorial, globals(), verbose=True)

# class TestTextbookFunctions(unittest.TestCase):

#     def test_factorial(self):
#         self.assertEqual(factorial(0), 1)
#         self.assertEqual(factorial(1), 1)
#         self.assertEqual(factorial(5), 120)
#         self.assertEqual(factorial(10), 3628800)

#     def test_fibonacci(self):
#         self.assertEqual(fibonacci(0), 0)
#         self.assertEqual(fibonacci(1), 1)
#         self.assertEqual(fibonacci(2), 1)
#         self.assertEqual(fibonacci(5), 5)
#         self.assertEqual(fibonacci(10), 55)

#     def test_is_palindrome(self):
#         self.assertTrue(is_palindrome("level"))
#         self.assertTrue(is_palindrome("A man a plan a canal Panama"))
#         self.assertFalse(is_palindrome("hello"))
#         self.assertTrue(is_palindrome(""))
#         self.assertTrue(is_palindrome("a"))

#     def test_count_words(self):
#         self.assertEqual(count_words("hello world"), 2)
#         self.assertEqual(count_words("this is a test"), 4)
#         self.assertEqual(count_words(""), 0)
#         self.assertEqual(count_words("oneword"), 1)

#     def test_is_prime(self):
#         self.assertFalse(is_prime(1))
#         self.assertTrue(is_prime(2))
#         self.assertTrue(is_prime(3))
#         self.assertFalse(is_prime(4))
#         self.assertTrue(is_prime(17))
#         self.assertFalse(is_prime(100))
#         self.assertTrue(is_prime(101))

# if __name__ == "__main__":
#     unittest.main()
