import http
import requests
from pathlib import Path
import json
import matplotlib.pyplot as pp
import numpy as np

try:
    response = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR&api_key=1b0999003f21c3fddb9eee4176bf5c42afc5e21a9353435e84727e529309c353')
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

# lets read whole file into numpy 2d array

data=np.loadtxt(fname='output.txt', delimiter=',')
print(data)

# split into 2 arrays
X=[]
Y=[]

# Ask the user for input
x_input = input("Enter a value for x: ")
y_input = input("Enter a value for y: ")

# Convert the user input to float values and append to arrays
X.append(float(x_input))
Y.append(float(y_input))

for i in range(len(data)):
    for j in range(2):
        if j==0:
            X.append(data[i] [j])
        else:
            Y.append(data[i] [j])
print(X)
print(Y)

pp.plot(X,Y)
pp.xlabel('X')
pp.ylabel('Y')
pp.title('')
pp.show()











# try:
#     response = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR&api_key=1b0999003f21c3fddb9eee4176bf5c42afc5e21a9353435e84727e529309c353')
#     # response.raise_for_status()
#     # access JSOn content
#     jsonResponse = response.json()
#     print("Entire JSON response")
#     print(jsonResponse)
#     json_obj=json.dumps(jsonResponse)
#     with open('D:\hackathon_2\DI_Hackathon_2\data1.txt', 'w') as f:
#         f.write(json_obj)
#     if response.status_code == 200:
#         with open('D:\hackathon_2\DI_Hackathon_2\data1.txt', 'w') as file:
#             file.write(response.text)
#             print('Data written to file successfully.')
#             file.close()
    

# except HTTPError as http_err:
#     print(f'HTTP error occurred: {http_err}')
# except Exception as err:
#     print(f'Other error occurred: {err}')


