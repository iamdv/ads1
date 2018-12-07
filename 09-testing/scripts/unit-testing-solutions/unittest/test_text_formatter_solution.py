import unittest

import text_formatter_solution

class TestTextFormatter(unittest.TestCase):

    def test_simple_text(self):
        input_text = "Cambridge Spark"
        border = "================="
        expected = " CAMBRIDGE SPARK \n" + border

        output = text_formatter_solution.make_heading(input_text)

        self.assertEqual(expected, output)

    def test_empty_text(self):
        input_text = ""

        output = text_formatter_solution.make_heading(input_text)

        expected = ""
        self.assertEqual(output, expected)

    def test_text_one_character(self):
        input_text = "a"

        output = text_formatter_solution.make_heading(input_text)

        expected = " A \n==="
        self.assertEqual(output, expected)

    def test_raises_when_title_too_long(self):
        input_text = "a" * 70

        with self.assertRaises(ValueError):
            text_formatter_solution.make_heading(input_text)
