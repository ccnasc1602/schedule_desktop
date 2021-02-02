import os, json, requests


class BaseRequests:
    def __init__(self):
        self.requests = requests
        try:
            with open('config.json') as file:
                self.url_base = json.load(file)
        except:
            self.url_base = 'http://localhost:8000/'

        self.headers = {
            'content-type': 'application/json',
            'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def post(self, url_api, body):
        url = self.url_base + url_api

        return self.__parseToJson(requests.post(
            url=url,
            data=json.dumps(body),
            headers=self.headers
        ))

    def put(self, url_api, body):
        url = self.url_base + url_api

        return self.__parseToJson(requests.put(
            url=url + str(body['id']) + '/',
            data=json.dumps(body),
            headers=self.headers
        ))

    def delete(self, url_api, body):
        url = self.url_base + url_api

        return self.__parseToJson(requests.delete(
            url=url + str(body['id']) + '/',
            data=json.dumps(body),
            headers=self.headers
        ))

    def get(self, url_api, parms={}):

        url = self.url_base['server_address'] + url_api
        print(url)
        return self.__parseToJson(self.requests.get(
            url=url,
            params=parms,
            headers=self.headers
        ))

    @staticmethod
    def __parseToJson(data):
        """
        Parse server response to JSON
        """
        if data.status_code in (200, 201):
            return data.json()
        else:
            return {'erro': data.status_code}


if __name__=='__main__':
    R = BaseRequests()
    ret = R.get('user/', {'username': 'luiza'})
    from pprint import pprint
    pprint(ret)
