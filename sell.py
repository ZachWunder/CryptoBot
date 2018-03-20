from bittrex import *
import datetime
class Sell:

	def __init__(self, buyObject):
		self.relative = buyObject.relative
		self.quantity = buyObject.getAmountBought()
		with open('secrets.txt', 'r') as secrets:
			total = secrets.readline().split(" ")
			apiKey = total[0]
			apiSecret = total[1]
		self.my_bittrex = Bittrex(apiKey, apiSecret)

	def calcLevels(self):
		levels = []
		for i in range(1, 7):
			self.relative += .03 * self.relative
			levels.append(self.relative)
		return levels
	
	def getPositionSize(self):
		return 8.33 * self.quantity
			

	def createsSellOrders(self):		
		self.my_bittrex.trade_sell(market="USDT-ADA", order_type='LIMIT', quantity=getpositionSize(), rate=.95 * self.relative, time_in_effect='GOOD_TIL_CANCELLED')
		for i in levels:
			self.my_bittrex.trade_sell(market="USDT-ADA", order_type='LIMIT', quantity=getpositionSize(), rate=i, time_in_effect='GOOD_TIL_CANCELLED')
		for j in my_bittrex.get_order_history()['result']:
			if j['TimeStamp'][:16] == datetime.datetime.utcnow().strftime("20%y-%m-%dT%H:%M"):
				self.orders[j['Limit']] = j['OrderUuid']