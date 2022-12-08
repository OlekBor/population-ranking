from api_connector import RandomDataAPI as randAPI
from api_connector import CountriesAPI
from country import Country

def user_input(lim: tuple[int, int]):
    lim_str = "[{} {})".format(*lim)
    quantity = int(input(f"How much random countries would you like to generate {lim_str}: "))
    while quantity not in range(*lim):
        quantity = int(input(f"Wrong input, try again in range {lim_str} [or Ctrl+D to exit]: "))
    return quantity

def search_country_info(country: str):
    country_orig = country
    country = country.lower()
    search_results = CountriesAPI().name_search(country.split(" ")[0])
    if isinstance(search_results, dict):
        print(f"Country not found: {country}")
        return None
    if len(search_results) == 1 or \
        country == 'Saint Barthelemy':
        return search_results[0]
    
    for result in search_results:
        if result['name']['common'].lower() == country or \
            result['name']['official'].lower() == country or \
            country_orig in result['altSpellings']:
            return result

def present(countries: list):
    for country in countries:
        country.display()

def main():
    quantity = user_input((5, 21))
    countries_names = randAPI().n_random_countries(quantity)
    print(f"Random countries: {countries_names}\n")

    countries_collection = [Country(country, search_country_info(country)) for country in countries_names]
    countries_collection = sorted(countries_collection, key=lambda country: country.get_population(), reverse=True)
    present(countries_collection)

if __name__ == "__main__":
    main()