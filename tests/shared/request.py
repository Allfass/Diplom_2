import requests


class TestRequests():
    def __init__(self, url, payload = "", token = "") -> None:
        self.url = url
        self.payload = payload
        self.header = {
            'Authorization': token
        }

    def get_empty_body(self):
        if self.header['Authorization']:
            return requests.post(self.url, headers=self.header, timeout=10)
        else:
            return requests.post(self.url, timeout=10)
    
    def post(self):
        if self.header['Authorization']:
            return requests.post(self.url, headers=self.header, data=self.payload, timeout=10)
        else:
            return requests.post(self.url, data=self.payload, timeout=10)
        
    def get(self):
        if self.header['Authorization']:
            return requests.get(self.url, headers=self.header, data=self.payload, timeout=10)
        else:
            return requests.get(self.url, data=self.payload, timeout=10)
