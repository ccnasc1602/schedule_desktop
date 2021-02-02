from base import BaseRequests


class User(BaseRequests):
    def __init__(self):
        super(User, self).__init__()
        self.url_api = 'user/'

    def get_list(self):
        return self.get(self.url_api)

    def get_detail(self, parms):
        return self.get(self.url_api, parms=parms)


if __name__=='__main__':
    U = User()
    print(U.get_list())
    parms = {'username': 'luiza'}
    print(U.get_detail(parms=parms))
