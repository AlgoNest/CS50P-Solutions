import sys
import requests
import json
if len(sys.argv) == 2:
    try:
      vaule = float(sys.argv[1])
    except:
      sys.exit("Command-line argument is not a number")
else:
    sys.exit("Missing command-line argument")
try:
   response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
   O = response.json()
   X = O["bpi"]["USD"]["rate_float"]
   TotalAmount = float(X) * vaule
   print(f"${TotalAmount:,.4f}")
except requests.RequestException:
   print("requests.RequestException")





