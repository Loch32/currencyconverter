#this is the second test build and also does not use the API

IntCurrency = input("Please choose the initial currency, using a three-letter ISO 4217 currency code. If you are unsure of what code your currency is, type 'help': ")

#ensuring that there's no confusion on how to format the country code

if IntCurrency == "AUD":
        IntCurAmount = int(input("Please enter the initial currency amount as a decimal: "))
elif IntCurrency == "help":
      print("For a list of currency codes visit: https://en.wikipedia.org/wiki/ISO_4217#List_of_ISO_4217_currency_codes")
else: print("Please try a different country code. At the moment, this converter only supports AUD, EUR, GBP, and USD.")

TargCurrency = input("Please choose the target currency, using a three-letter ISO 4217 currency code: ")
if TargCurrency == "GBP":
      result = IntCurAmount * 0.65
      print(IntCurAmount, IntCurrency, "is equal to", result, TargCurrency)
else: print("Please try again.")   