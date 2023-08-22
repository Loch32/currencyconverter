#this one attempts to use the currencyconverter library

from currency_converter import CurrencyConverter

IntCurrency = input("Please choose the initial currency, using a three-letter ISO 4217 currency code. If you are unsure of what code your currency is, type 'help': ").upper()

if IntCurrency == "AUD":
        IntCurAmount = float(input("Please enter the initial currency amount as a decimal: "))
elif IntCurrency == "HELP":
      print("For a list of currency codes visit: https://en.wikipedia.org/wiki/ISO_4217#List_of_ISO_4217_currency_codes")
      #typing "help" prints this string, linking to the wikipedia article that contains the correct currency codes.
      IntCurrency = input("Please choose the initial currency, using a three-letter ISO 4217 currency code: ").upper()
      IntCurAmount = float(input("Please enter the initial currency amount as a decimal: "))
else: print("Please try a different country code. At the moment, this converter only supports AUD, EUR, GBP, and USD.")
# this code ^^^^^^^^^ (lines 7-14) were fixed by @Blep-JurassicJelly

TargCurrency = input("Please choose the target currency, using a three-letter ISO 4217 currency code: ").upper()
if TargCurrency == "GBP":
      result = IntCurAmount * 0.5
       #i havent worked out how to use any apis or libraries yet so this is using a fixed exchange rate as of 16/08/23
      print(IntCurAmount, IntCurrency, "is equal to", result, TargCurrency)
else: print("Please try again.")