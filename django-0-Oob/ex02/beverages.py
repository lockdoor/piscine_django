class HotBeverage():

	def __init__(self, price=0.30, name="hot beverage"):
		self.price = price
		self.name = name

	def description(self):
		return HotBeverage.Description("Just some hot water in a cup.")

	class Description():
		def __init__(self, msg):
			self.msg = msg
		def __str__(self):
			return self.msg

	def __str__(self):
		return f'name : {self.name}\nprice : {self.price}\ndescription : {self.description()}'

class Coffee(HotBeverage):
	def __init__(self):
		super().__init__(0.40, "coffee")

	def description(self):
		return super().Description("A coffee, to stay awake.")

class Tea(HotBeverage):
	def __init__(self):
		super().__init__(0.30, "tea")

class Chocolate(HotBeverage):
	def __init__(self):
		super().__init__(0.50, "chocolate")

	def description(self):
		return super().Description("Chocolate, sweet chocolate...")

class Cappuccino(HotBeverage):
	def __init__(self):
		super().__init__(0.45, "cappuccino")

	def description(self):
		return super().Description("Un po’ di Italia nella sua tazza!")


def my_func():
	print (HotBeverage())
	print (Coffee())
	print (Tea())
	print (Chocolate())
	print (Cappuccino())

if __name__ == '__main__':
	my_func()