# API Link: https://api.coindesk.com/v1/bpi/currentprice.json

# Importing libraries
import json
import sys
import requests

# take in 1 command line argument n (num of bitcoin) that must be able
# to be converted into a float; else sys.exit("Error message")
if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    except ValueError:
        print("Invalid Argument")
else:
    sys.exit("Invalid Argument Count")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    print(
        " There was an ambiguous exception that occurred while handling your request."
    )

rate = response.json()["bpi"]["USD"]["rate_float"]
amount = rate * float(sys.argv[1])

# Output the current cost of Bitcoins in USD to four
# decimal places, using comma as a thousands separator.
print(f"${amount:,.4f}")
