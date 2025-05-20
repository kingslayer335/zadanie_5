import requests
class CurrencyList:
    def __init__(self, url):
        # tworzy zapytanie get do api i zmienia odpowiedz na json
        self.response = requests.get(url)
        self.data = self.response.json()
        # zamienia jsona na liste par
        self.pairs = [(code, name) for code, name in self.data.items() if name]
        self.formatted_pairs = [f'{code.upper()} : {name.capitalize()}' for code, name in self.pairs]
    def get_currency_code(self, currency_name):
        for code, name in self.data.items():
            if name.lower() == currency_name.lower():
                return f'{code.upper()} : {name.capitalize()}'
        return None
    def get_currency_name(self, currency_code):
        for code, name in self.pairs:
            if code.lower() == currency_code.lower():
                return f'{code.upper()} : {name.capitalize()}'
        return None
    def get_pairs(self):
        return self.formatted_pairs
