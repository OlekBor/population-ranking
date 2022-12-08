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
        if "Antarctica" in self.name:
            return "No capital"
        if self.json["capital"]:
            return self.json["capital"][0]

    def get_population(self):
        try:
            if not self.json:
                return 0
            if self.json["population"]:
                return self.json["population"]
        except Exception as t:
            print(f"{t}\n{self.name}")

    def get_languages(self):
        if not self.json:
            return "No information found!"
        if any(self.json["languages"].values()):
            return list(self.json["languages"].values())