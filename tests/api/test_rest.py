import unittest
from tests.test_utils import *
from src.db.library import rebuild_tables

class TestRest(unittest.TestCase):

    def set_up(self):
        rebuild_tables()

    def test_get_all_users(self):
        expected = {
            '1': {
                'name': 'Ada Lovelace',
                'contact': 'ALovelace@gmail.com'
            },
            '2': {
                'name': 'Mary Shelley',
                'contact': 'MShelley@gmail.com'
            },
            '3': {
                'name': 'Jackie Gleason',
                'contact': 'JGleason@gmail.com'
            },
            '4': {
                'name': 'Art Garfunkel',
                'contact': 'AGarfunkel@gmail.com'
            }
        }

        actual = get_rest_call(self, 'http://localhost:5000/users')
        self.assertEqual(expected, actual)
        self.assertEqual(4, actual.__len__())

    def test_get_all_books(self):
        expected = 10   # total number of books
        actual = get_rest_call(self, 'http://localhost:5000/books')
        self.assertEqual(expected, actual.__len__())

    def test_get_fiction_books(self):
        expected = 6
        actual = get_rest_call(self, 'http://localhost:5000/books/fiction')
        self.assertEqual(expected, actual.__len__())

    def test_get_nonfiction_books(self):
        expected = 4
        actual = get_rest_call(self, 'http://localhost:5000/books/non-fiction')
        self.assertEqual(expected, actual.__len__())

    def test_search_by_author(self):
        # single search term
        expected = {
            '8': {
                'title': 'To Kill a Mockingbird',
                'type': 'Fiction',
                'author': 'Harper Lee',
                'publish date': 1960,
                'summary': 'Chronicles the childhood of Scout and Jem Finch',
                'copies': 1,
                'available at': 'Fairport, Henrietta'
            }
        }
        actual = get_rest_call(self, 'http://localhost:5000/books/Harper Lee')
        self.assertEqual(expected, actual)

        # author does not exist
        actual = get_rest_call(self, 'http://localhost:5000/books/Stephen King')
        self.assertEqual([], actual)

    def test_search_by_title(self):
        # single search term
        expected = {
            '7': {
                'title': 'The Lightning Thief',
                'type': 'Fiction',
                'author': 'Rick Riordan',
                'publish date': 2005,
                'summary': 'A 12 year-old boy who learns that his true father is Poseidon',
                'copies': 4,
                'available at': 'Penfield, Fairport, Henrietta'
            }
        }
        actual = get_rest_call(self, 'http://localhost:5000/books/The Lightning Thief')
        self.assertEqual(expected, actual)

        # title does not exist
        actual = get_rest_call(self, 'http://localhost:5000/books/Harry Potter')
        self.assertEqual([], actual)

    def test_search_fiction_and_author(self):
        # multiple search terms - fiction books by this author
        expected = {
            "5": {
                "title": "The Dead Romantics",
                "type": "Fiction",
                "author": "Ashley Poston",
                "publish date": 2022,
                "summary": "The main character is a ghostwriter for a romance novelist",
                "copies": 6,
                "available at": "Penfield, Fairport, Henrietta, Pittsford"
            }
        }
        actual = get_rest_call(self, 'http://localhost:5000/books/fiction/Ashley Poston')
        self.assertEqual(expected, actual)

        # does not exist
        actual = get_rest_call(self, 'http://localhost:5000/books/fiction/Batman')
        self.assertEqual([], actual)

    def test_search_nonfiction_and_title(self):
        # multiple search terms - non-fiction books with this title
        expected = {
            "4": {
                "title": "The Princess Spy",
                "type": "Non-fiction",
                "author": "Larry Loftis",
                "publish date": 2022,
                "summary": "Follows the hidden history of an ordinary American girl who became one of the most daring WWII spies",
                "copies": 2,
                "available at": "Penfield, Fairport"
            }
        }
        actual = get_rest_call(self, 'http://localhost:5000/books/non-fiction/Larry Loftis')
        self.assertEqual(expected, actual)

        # does not exist
        actual = get_rest_call(self, 'http://localhost:5000/books/non-fiction/Endgame')
        self.assertEqual([], actual)