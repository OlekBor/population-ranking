import requests

class APIConnector():

    def __init__(self, base_uri: str):
        self.base_uri = base_uri

    def set_base_uri(uri: str):
        self.base_uri = uri

    def get(self, endpoint: str):
        return requests.get(self.base_uri + endpoint)

if __name__ == "__main__":
    api = APIConnector("https://random-data-api.com/api/v2/")
    print(api.get("users").text)