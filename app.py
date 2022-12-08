from api_connector import RandomDataAPI as randAPI

def user_input(lim: tuple[int, int]):
    lim_str = "[{} {})".format(*lim)
    quantity = int(input(f"How much random countries would you like to generate {lim_str}: "))
    while quantity not in range(*lim):
        quantity = int(input(f"Wrong input, try again in range {lim_str} [or Ctrl+D to exit]: "))
    return quantity

def main():
    quantity = user_input((5, 21))
    countries = randAPI().n_random_countries(quantity)
    print(countries)

if __name__ == "__main__":
    main()