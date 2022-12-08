from api_connector import RandomDataAPI

def n_random_countries(quantity: int):
    random_data_api = RandomDataAPI()
    countries = []
    while len(countries) < quantity:
        country = random_data_api.new_random_address()['country']
        if country in countries:
            continue
        countries.append(country)
    return countries

def main():
    quantity = int(input("How much random countries would you like to generate: "))
    countries = n_random_countries(quantity)
    print(countries)

if __name__ == "__main__":
    main()