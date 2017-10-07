class Product(object):
	def __init__(self, price, item_name, weight, brand, cost):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = "for sale"

	def __str__(self):
		return "{}\nPrice: {}\nItem Name: {}\nWeight: {}\nBrand: {}\nCost: {}\nStatus: {}\n{}\n".format('{', self.price, self.item_name, self.weight, self.brand, self.cost, self.status, '}')

	def Sell(self):
		self.status = "sold"
		return self

	def AddTax(self, tax):
		self.price*=(1+tax)
		return self

	def Return(self, returnReason):
		if returnReason == "defective":
			self.status = "defective"
			self.price = 0
		elif returnReason == "returnUnopenedBox":
			self.status = "for sale"
		elif returnReason == "returnOpenedBox":
			self.status = "used"
			self.price*=0.8
		return self

	def DisplayInfo(self):
		print self
		return self

product1 = Product(50, "jacket", "2lbs", "H&M", "20")
product1.DisplayInfo().Sell().DisplayInfo().AddTax(.15).DisplayInfo().Return("returnUnopenedBox").DisplayInfo().Return("returnOpenedBox").DisplayInfo().Return("defective").DisplayInfo()