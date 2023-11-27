import requests
import sys

def main():
    c_c = get_price() * check_input()
    print(f"${c_c:, .4f})

def get_price():
    #function to get price of btc from coinmarket cap
    try:#error handling block of the request from coincap
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        print("There is an issue with the request")

    r = response.json()
    cp = float(r["bpi"["USD"["rate"]]])
    return cp

def check_input():
    #function to check command line argument
    try:
        n = float(sys.argv[1])
        if sys.argv != 2:
            raise IndexError
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        return n



main()


