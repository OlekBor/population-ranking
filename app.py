from api_connector import RandomDataAPI as randAPI
from api_connector import CountriesAPI

def user_input(lim: tuple[int, int]):
    lim_str = "[{} {})".format(*lim)
    quantity = int(input(f"How much random countries would you like to generate {lim_str}: "))
    while quantity not in range(*lim):
        quantity = int(input(f"Wrong input, try again in range {lim_str} [or Ctrl+D to exit]: "))
    return quantity

def search_country_info(country: str):
    country = country.lower()
    search_results = CountriesAPI().name_search(country.split(" ")[0])
    if len(search_results) == 1:
        return search_results[0]
    for result in search_results:
        if country in result['name']['common'].lower() or country in result['name']['official'].lower():
            return result
        if result['name']['common'].lower() == country.split(',')[0] or result['name']['official'].lower() == country.split(',')[0]:
            return result
    print(f"Country not found: {country}")
    return -1

def present(countries: list):
    for country_info in countries:
        print(f"{country_info['name']['common']}:")
        print(f"\t{country_info['capital'][0]}")
        print(f"\t{country_info['population']}")
        print(f"\t{list(country_info['languages'].values())}")
        print()

def main():
    quantity = user_input((5, 21))
    countries_names = randAPI().n_random_countries(quantity)
    print(f"Random countries: {countries}\n")

    countries_details = [search_country_info(country) for country in countries_names]
    countries_details = sorted(countries_details, key=lambda country: country["population"], reverse=True)
    present(countries_details)

if __name__ == "__main__":
    main()