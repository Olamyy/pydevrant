import unittest
from devrant import devrant


class DevRantTest(unittest.TestCase):
    config_dict = {'search_term': 'python', 'rant_id': '', 'username': 'idanSh', 'user_id': '555642'}

    def test_search_rants_with_keyword(self):
        response = devrant.search_rants(self.config_dict['search_term'])
        assert response.get('success') is True

    def test_search_rants_with_no_keyword(self):
        response = devrant.search_rants()
        assert response.get('success') is True

    def test_get_rants(self):
        response = devrant.get_rants()
        assert response.get('success') is True

    def test_get_rant(self):
        response = devrant.get_rant(self.config_dict['rant_id'])
        assert response.get('success') is True

    def test_get_user_id(self):
        response = devrant.get_user(self.config_dict['username'])
        assert response.get('success') is True

    def test_get_user_profile(self):
        response = devrant.get_user_profile(self.config_dict['user_id'])
        assert response.get('success') is True

if __name__ is '__main__':
    unittest.main()
