import request
import sys

try:
    request.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except request.RequestException:
    print("There is an issue with the request")
    
