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