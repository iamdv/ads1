import unittest
import courses

class TestCourses(unittest.TestCase):

    def test_empty_string(self):
        input_identifier = ""
        result = courses.is_valid_identifier(input_identifier)
        self.assertFalse(result)

    def test_good_identifier(self):
        input_identifier = "C103"
        result = courses.is_valid_identifier(input_identifier)
        self.assertTrue(result)

    def test_bad_identifier_too_long(self):
        input_identifier = "C1031"
        result = courses.is_valid_identifier(input_identifier)
        self.assertFalse(result)