import unittest
from hamcrest import *


class TestHamcrest(unittest.TestCase):

    def test_word_contained_in_description(self):
        description = "This is a cool exercise"
        self.assertTrue("cool" in description)

    def test_description_starts_with(self):
        description = "This is a cool exercise"
        self.assertTrue(description[0:4] == "This")

    def test_user_has_a_name(self):
        user = {"name":"Tom", "id": 1337}
        self.assertTrue("name" in user)

    def test_list_has_length_of_ten(self):
        sensors_information = [18, 19, 20, 17, 19]
        expected_length = 5
        self.assertTrue(len(sensors_information) == expected_length)

    def test_list_is_empty(self):
        data = []
        self.assertTrue(len(data) == 0)