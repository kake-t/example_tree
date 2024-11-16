import unittest
from example_tree.greeting.hello import hello_world


class TestCalculator(unittest.TestCase):
    def test_hello_world(self):
        """hello world.のテスト"""
        self.assertEqual(hello_world(), "hello world.")
