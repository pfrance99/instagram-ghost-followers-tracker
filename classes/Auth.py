from instagram_private_api import Client

class Auth:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def connect(self):
        return Client(self.username, self.password)
