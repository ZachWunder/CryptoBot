#RetrieveData
import app
from bittrex import *
import os

my_bittrex = Bittrex(os.environ["BITTREX_KEY"], os.environ["BITTREX_SECRET"])

data = app.getClosingPrices('USDT-ADA', 100000, "thirtyMin")

with open('data.txt', 'w') as dataFile:
	for i in data[1:]:
		dataFile.write("{}\n".format(i))
	dataFile.write("0.0\n0.0")
