class Country:
    def __init__(self, name: str, json: dict):
        self.name = name
        self.json = json

    def display(self):
        print(f"{self.name}:")
        print(f"\t{self.get_capital()}")
        print(f"\t{self.get_population()}")
        print(f"\t{self.get_languages()}")

    def get_capital(self):
        if not self.json:
            return "No information found!"
        try:
            return self.json["capital"][0]
        except KeyError:
            return "No information found!"

    def get_population(self):
        if not self.json:
            return 0
        try:
            return self.json["population"]
        except KeyError:
            return 0

    def get_languages(self):
        if not self.json:
            return "No information found!"
        try:
            return list(self.json["languages"].values())
        except KeyError:
            return "No information found!"