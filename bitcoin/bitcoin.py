import requests
import sys

try:#error handling block of the request from coincap
    response = request.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except request.RequestException:
    print("There is an issue with the request")

r = response.json()
cp = float(r["bpi"["USD"["rate"]]])



