from base import PyDevRantAPI


class Devrant(PyDevRantAPI):
    def __init__(self):
        super(Devrant, self).__init__()

    def search_rants(self, keyword=None):
        """
        
        :param keyword: 
        :return: 
        """
        keyword = keyword if keyword else "i love devrant"
        endpoint = self._search_url.format(keyword)
        request = self._exec_request('GET', endpoint)
        return request

    def get_rant(self, rant_id):
        """
        
        :param rant_id: 
        :return: 
        """
        endpoint = self._rant_url.format(rant_id)
        request = self._exec_request('GET', endpoint)
        return request

    def get_rants(self, sort="algo"):
        """
        Return all rants, sorted by @sort 
        :type sort: object
        :return: 
        """
        endpoint = self._rants_url.format(sort)
        request = self._exec_request('GET', endpoint)
        return request

    def get_user(self, username):
        """
        Get UserID from username
        :param username: 
        :return: 
        """
        endpoint = self._user_url.format(username)
        request = self._exec_request('GET', endpoint)
        return request

    def get_user_profile(self, user_id):
        """
        Get a user's profile given its user_id
        :param user_id: 
        :return: 
        """
        endpoint = self._profile_url.format(user_id)
        request = self._exec_request('GET', endpoint)
        return request

devrant = Devrant()

