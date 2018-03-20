from bittrex import *
import datetime
class Buy:

	def __init__(self, rel):
		self.relative = rel
		self.levels = self.getLevels()
		with open('secrets.txt', 'r') as secrets:
			total = secrets.readline().split(" ")
			apiKey = total[0]
			apiSecret = total[1]
		self.my_bittrex = Bittrex(apiKey, apiSecret)
		self.orders = {}

	def getLevels(self):
		levels = []
		for time in range(0, 25):
			levels.append((self.relative * (.990745441) ** (time)) - (.05 * self.relative))
		return levels


	def getCompletedOrders(self):
		completedOrdersID = []
		for i in self.orders:
			if self.my_bittrex.get_order(orders.get(i))['result']['QuantityRemaining'] == 0:
				completedOrdersID.append(i)
		return completedOrdersID

	def getAmountBought(self):
		total = 0
		for i in self.getCompletedOrders():
			total += self.my_bittrex.get_order(i)['result']['Quantity']
		return total

	def getIncompleteOrders(self):
		incompleteOrdersID = []
		for i in self.orders:
			if self.orders.get(i) != 0:
				incompleteOrdersID.append(i)
		return incompleteOrdersID

	def getPositionSize(self):
		accountSize = self.my_bittrex.get_balance("USDT")['result']['Balance']
		#       VV % increase per level
		return .02 * (accountSize / 2)

	def createBuyOrders(self):
		for i in levels:
			self.my_bittrex.trade_buy(market="USDT-ADA", order_type='LIMIT', quantity=getpositionSize(), rate=i, time_in_effect='GOOD_TIL_CANCELLED')
		for j in my_bittrex.get_order_history()['result']:
			if j['TimeStamp'][:16] == datetime.datetime.utcnow().strftime("20%y-%m-%dT%H:%M"):
				self.orders[j['Limit']] = j['OrderUuid']
				









