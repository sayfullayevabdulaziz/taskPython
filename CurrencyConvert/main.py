# Python program to convert the currency
# of one country to that of another country

# Import the modules needed
import requests


class Currency_convertor:
    # empty dict to store the conversion rates
    rates = {}

    def __init__(self, url, apikey):
        data = requests.get(url, headers={"apikey": apikey}).json()

        # Extracting only the rates from the json data
        self.rates = data["result"]

    # function to do a simple cross multiplication between
    # the amount and the conversion rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount

        # if from_currency != 'EUR':
        #     amount = amount / self.rates[from_currency]

        # limiting the precision to 2 decimal places
        amount = round(self.rates, 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))


# Driver code
if __name__ == "__main__":
    # YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io'

    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = int(input("Amount: "))

    url = f'https://api.apilayer.com/fixer/convert?to={to_country}&from={from_country}&amount={amount}'
    apikey = "yzfRmhm63E2A960TsJxWe4CLk0DRVjlf"
    currency = Currency_convertor(url, apikey)


    currency.convert(from_country, to_country, amount)



# https://www.geeksforgeeks.org/currency-converter-in-python/