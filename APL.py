import http
import requests
from pathlib import Path
import json
import matplotlib.pyplot as pp
import matplotlib.pyplot as plt
import numpy as np

try:
    response = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR,SGD,INR,CAD,AUD&api_key=1b0999003f21c3fddb9eee4176bf5c42afc5e21a9353435e84727e529309c353')
    # # response.raise_for_status()
    # access JSOn content
    # response = requests.get('https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest?fsym=BTC&api_key=1b0999003f21c3fddb9eee4176bf5c42afc5e21a9353435e84727e529309c353')
    jsonResponse = response.json()
    print("Entire JSON response")
    print(jsonResponse)
#//////// displaying data into a text file
    if response.status_code == 200:
        with open('output.txt', 'w') as outfile:
            json.dump(jsonResponse, outfile, indent=4)
            print('Data written to file successfully.')
            


    

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')


usd_price = jsonResponse["RAW"]["BTC"]["USD"]["PRICE"]
euro_price = jsonResponse["RAW"]["BTC"]["EUR"]["PRICE"]
cad_price = jsonResponse["RAW"]["BTC"]["CAD"] ["PRICE"]
sgd_price = jsonResponse["RAW"]["BTC"]["SGD"] ["PRICE"]

# Price
# 
#
#       |
#       |      |
#       |      |
##################>
#     USD    EURO

x_axis =["USD","EURO","CAD","SGD"]
y_axis = [usd_price, euro_price,cad_price,sgd_price]

 
# creating the bar plot
plt.bar(x_axis, y_axis, color ='maroon',
        width = 0.4)

plt.xlabel("CURRENCY")
plt.ylabel("PRICE")
plt.title("BTC")
plt.show()





