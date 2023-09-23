import requests

class CountryDataFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_all_data(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to fetch data. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching data: {e}")

    def display_country_info(self):
        data = self.fetch_all_data()
        if data:
            for country in data:
                name = country.get('name', 'N/A').get('common', 'N/A')
                currencies = country.get('currencies', [])
                currency_names = ', '.join([currencies.get(currency, 'N/A').get('name', 'N/A') for currency in currencies])
                currency_symbols = ', '.join([currencies.get(currency, 'N/A').get('symbol', 'N/A') for currency in currencies])
                print(f"Country: {name}, Currencies: {currency_names}, Currency Symbols: {currency_symbols}")

    def display_countries_with_dollar(self):
        data = self.fetch_all_data()
        if data:
            for country in data:
                name = country.get('name', 'N/A').get('common', 'N/A')
                currencies = country.get('currencies', [])
                currency_names = ', '.join([currencies.get(currency, 'N/A').get('name', 'N/A') for currency in currencies])
                if "ollar" in currency_names:
                   print(f"Country: {name}")


    def display_countries_with_euro(self):
        data = self.fetch_all_data()
        if data:
            for country in data:
                name = country.get('name', 'N/A').get('common', 'N/A')
                currencies = country.get('currencies', [])
                currency_names = ', '.join([currencies.get(currency, 'N/A').get('name', 'N/A') for currency in currencies])
                if "Euro" in currency_names:
                   print(f"Country: {name}")


# URL for fetching country data
url = "https://restcountries.com/v3.1/all"

# Create an instance of the CountryDataFetcher class
data_fetcher = CountryDataFetcher(url)

# Display country information
print("Country Information:")
data_fetcher.display_country_info()

# Display countries with Dollar as currency
print("\nCountries with Dollar currency:")
data_fetcher.display_countries_with_dollar()

# Display countries with Euro as currency
print("\nCountries with Euro currency:")
data_fetcher.display_countries_with_euro()
