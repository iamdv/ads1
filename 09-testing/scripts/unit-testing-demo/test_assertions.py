import unittest


class TestAssertions(unittest.TestCase):

    def test_bad(self):
        value = 42
        expected = 43

        self.assertTrue(value == expected)

    def test_good(self):
        value = 42
        expected = 43

        self.assertEqual(value, expected)