import requests

class APIConnector():

    def __init__(self, base_uri: str):
        self.base_uri = base_uri

    def set_base_uri(uri: str):
        self.base_uri = uri

    def get(self, endpoint: str):
        return requests.get(self.base_uri + endpoint)

class RandomDataAPI(APIConnector):

    def __init__(self, base_uri='https://random-data-api.com/api/v2/'):
        super().__init__(base_uri)

    def new_random_address(self):
        request_result = self.get("addresses")
        return request_result.json()

class CountriesAPI(APIConnector):

    def __init__(self, base_uri='https://restcountries.com/v3.1/'):
        super().__init__(base_uri)

    def name_search(self, name: str):
        return self.get(f"name/{name}").json()

if __name__ == "__main__":
    api_response = CountriesAPI().name_search("asdf")
    try:
        print(api_response[0]["population"])
    except KeyError:
        print("No information found")