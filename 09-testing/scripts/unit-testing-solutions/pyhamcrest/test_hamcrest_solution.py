import unittest
from hamcrest import *


class TestHamcrest(unittest.TestCase):

    def test_word_contained_in_description(self):
        description = "This is a cool exercise"
        assert_that(description, contains_string("cool"))

    def test_description_starts_with(self):
        description = "This is a cool exercise"
        assert_that(description, starts_with("This"))

    def test_user_has_a_name(self):
        user = {"name":"Tom", "id": 1337}
        assert_that(user, has_key("name"))

    def test_list_has_length_of_ten(self):
        sensors_information = [18, 19, 20, 17, 19]
        expected_length = 5
        assert_that(sensors_information, has_length(expected_length))

    def test_list_is_empty(self):
        data = []
        assert_that(data, is_(empty()))