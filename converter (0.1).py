#this first test build won't be using the api because i am dumb and haven't figured that bit out yet
#and i'm doing this way later than i should've

##### CODE SHAMELESSLY STOLEN FROM MR GIBBS START #####
exchange_rates = [
    {"currency": "AUD", "rate": 1.0},
    {"currency": "EUR", "rate": 0.85},
    {"currency": "GBP", "rate": 0.75},
    {"currency": "USD", "rate": 0.60},]
##### CODE SHAMELESSLY STOLEN FROM MR GIBBS END #####

IntCurrency = input("Please choose the initial currency, using a three-letter ISO 4217 currency code: ")

#ensuring that there's no confusion on how to format the country code

if IntCurrency == "AUD":
        IntCurAmount = int(input("Please enter the initial currency amount as a decimal: "))
else: print("Please try a different country code. At the moment, this converter only supports AUD, EUR, GBP, and USD.")

TargCurrency = input("Please choose the target currency, using a three-letter ISO 4217 currency code: ")

