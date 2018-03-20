import os
from bittrex import *
from Buy import Buy
from sell import Sell

with open('secrets.txt', 'r') as secrets:
	total = secrets.readline().split(" ")
	apiKey = total[0]
	apiSecret = total[1]

my_bittrex = Bittrex(apiKey, apiSecret)


def updateRelative():
	with open('relative.txt', 'r') as relativeFile:
		relative = relativeFile.readline()
	return float(relative)


def cleanOrders(buy):
	for i in buy.getIncompleteOrders():
		my_bittrex.cancel(i)

def withdraw(buy):
	my_bittrex.withdraw('ADA', buy.getAmountBought())
	
if __name__ == '__main__':
	relative = 100
	while True:
		newRelative = updateRelative()
		if (newRelative != relative):
			relative = newRelative
			buyPosition = Buy(relative)
			cleanOrders(buyPosition)
			sellPosition = Sell(buyPosition)
			buyPosition.createBuyOrders()
			
