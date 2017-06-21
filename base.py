import requests


class PyDevRantAPI(object):
    """
    """

    _content_type = "application/json"
    _base_dev_rant_api = "https://www.devrant.io/api/{0}?app=3{1}"
    _search_url = _base_dev_rant_api.format('devrant/search', '&term={0}')
    _user_url = _base_dev_rant_api.format('get-user-id', '&username={0}')
    _rants_url = _base_dev_rant_api.format('devrant/rants', '&sort={}')
    _rant_url = _base_dev_rant_api.format('devrant/rants{0}', '')
    _profile_url = _base_dev_rant_api.format('users/{}', '')

    def __init__(self):
        self.http_headers = {"Content-Type": self._content_type}

    def _json_parser(self, json_response):
        """Only the status code, the status of the request and the data
        is sent back. the message is irrelevant if ths request was successful"""
        response = json_response.json()
        return response

    def _exec_request(self, method, url):
        method_map = {
            'GET': requests.get,
                     }

        request = method_map.get(method)

        response = request(
            url, headers=self.http_headers, verify=True)
        if response.status_code in [404, 405]:
            return response.status_code
        body = response.json()
        if body.get('success') == 'false':
            return response.status_code, body['status']
        if response.status_code in [200, 201]:
            return self._json_parser(response)
        response.raise_for_status()