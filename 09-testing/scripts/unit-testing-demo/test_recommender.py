import unittest
from hamcrest import *

import recommender

class TestRecommender(unittest.TestCase):

    def test_has_matrix_as_favourite_movie_bad(self):

        USER = "Raoul"
        movies = recommender.find_movies_for(USER, ["Action", "Comedy"])

        self.assertTrue("Matrix" in movies)

    def test_has_matrix_as_favourite_movie_good(self):

        USER = "Raoul"
        movies = recommender.find_movies_for(USER, ["Action", "Comedy"])

        assert_that(movies, has_item("Matrix"))


    def test_has_correct_keyword_in_description(self):
        MOVIE = "Thor"
        description = recommender.description_for_movie(MOVIE)

        assert_that(description, contains_string("Asgarsd"))

