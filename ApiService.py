import requests

class ApiService:
    def get_data(self, url, endpoint, headers=None):
        res = requests.get(
            url=f'{url}{endpoint}',
            headers=headers
        )
        return res.json()

    def post_data(self, url, endpoint, json=None, headers=None):
        res = requests.post(
            url=f'{url}{endpoint}',
            json=json,
            headers=headers
        )
        return res.json()