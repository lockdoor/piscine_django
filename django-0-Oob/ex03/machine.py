from beverages import *
import random

class CoffeeMachine():
	menus: dict = {
		"hot beverage": HotBeverage, 
		"coffee": Coffee,
		"tea": Tea,
		"chocolate": Chocolate,
		"capuccino": Cappuccino
		}

	def __init__(self):
		self.cups = 0

	def repair(self):
		self.cups = 0

	def serve(self, order=None):
		if self.cups >= 10:
			raise BrokenMachineException
		if order is None:
			self.cups += 1
			return random.choice(list(self.menus.values()))()		
		cup = self.menus.get(order)
		if cup is None:
			return EmptyCup()
		self.cups += 1
		return cup()

class BrokenMachineException(Exception):
	def __init__(self):
		super().__init__("This coffee machine has to be repaired.")

def my_func():
	menus: list[str] = [
		"hot beverage", 
		"coffee",
		"tea",
		"chocolate",
		"capuccino"]
	coffee_machine = CoffeeMachine()
	print (coffee_machine.serve("coffee"))
	print (coffee_machine.serve("cola"))
	print (coffee_machine.serve())
	for x in range(15):
		try:
			print (coffee_machine.serve(random.choice(menus)))
		except BrokenMachineException as e:
			print (e)
			coffee_machine.repair()

if __name__ == '__main__':
	my_func()
