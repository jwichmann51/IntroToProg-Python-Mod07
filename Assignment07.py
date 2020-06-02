# ------------------------------------------------- #
# Title: Assignment07
# Description: Exception handling and pickling demo
# ChangeLog: (Who, When, What)
# JWichmann,5/31/2020,Created Script
# JWichmann,6/1/2020, final review of the script
# ------------------------------------------------- #

# Data -------------------------------------------- #
strTicker1 = str(input("Enter a Ticker: ")) # The user is asked to enter three stock tickers.
strTicker2 = str(input("Enter a 2nd Ticker: "))
strTicker3 = str(input("Enter a 3rd Ticker: "))
try:
    intPrice1 = int(input("Enter a price: ")) # The user is asked to enter three stock prices.
except:
    print("Please restart the program and enter prices only.") # Exception handing encourages the user enter a number and not a string.

try:
    intPrice2 = int(input("Enter a 2nd price: "))
except:
    print("Please restart the program and enter prices only.")

try:
    intPrice3 = int(input("Enter a 3rd price: "))
except:
    print("Please restart the program and enter prices only.")

# Process -------------------------------------------- #

import pickle

print("Research lists.")
prices = [intPrice1, intPrice2, intPrice3]
ticker = [strTicker1, strTicker2, strTicker3]
f = open("coverage.dat", "wb")
pickle.dump(prices, f)
pickle.dump(ticker, f)
f.close()

print("\nUnpickling lists.")
f = open("coverage.dat", "rb")
prices = pickle.load(f)
ticker = pickle.load(f)

# Presentation -------------------------------------------- #

print(ticker)
print(prices)
f.close()

input("\n\nPress the enter key to exit.")
