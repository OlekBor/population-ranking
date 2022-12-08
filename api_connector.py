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

    def n_random_countries(self, quantity: int):
        countries = []
        while len(countries) < quantity:
            country = self.new_random_address()['country']
            if country in countries:
                continue
            countries.append(country)
        return countries

class CountriesAPI(APIConnector):

    def __init__(self, base_uri='https://restcountries.com/v3.1/'):
        super().__init__(base_uri)

    def name_search(self, name: str):
        return self.get(f"name/{name}").json()

if __name__ == "__main__":
    print(RandomDataAPI().n_random_countries(7))