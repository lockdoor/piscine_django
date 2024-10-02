class Intern():
	def __init__(self, 
		name="My name? I’m nobody, an intern, I have no name."):
		self.Name = name

	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")

	def make_coffee(self):
		return Coffee()

	def __str__(self):
		return self.Name

class Coffee():
	def __str__(self):
		return "This is the worst coffee you ever tasted."

def my_func():
	try:
		bob = Intern()
		print (bob)
		print (bob.make_coffee())

		mark = Intern("Mark")
		print (mark)
		print (mark.make_coffee())

		john = Intern("John")
		print (john)
		print (john.work())
	except Exception as e:
		print(e)
	pass

if __name__ == '__main__':
	my_func()