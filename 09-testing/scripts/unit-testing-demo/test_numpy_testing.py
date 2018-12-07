import unittest
import numpy.testing as np


class TestNumpyTesting(unittest.TestCase):

    def test_float_addition_assertion(self):

        res = 0.1 + 0.2
        expected = 0.3

        self.assertEqual(res, expected)

    def test_float_addition_with_numpy(self):
        res = 0.1 + 0.2
        expected = 0.3

        np.assert_allclose(res, expected)