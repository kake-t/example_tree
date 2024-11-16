import unittest
from example_tree.greeting.hello import hello_python


class TestCalculator(unittest.TestCase):
    def test_hello_python(self):
        """hello python.のテスト"""
        self.assertEqual(hello_python(), "hello python.")
