import unittest
from base import *

from models.users_ import User


class TestRequest(unittest.TestCase):
    def test_post_user(self):
        request = User().get_list()
        response = request(user_data_fake)
        self.assertEqual(response.reason, 'Created')

    def test_put_user(self):
        pass

    def test_get_user_list(self):
        pass

    def test_get_user_detail(self):
        pass

    def test_delete_user(self):
        pass

if __name__=='__main__':
    unittest.main()