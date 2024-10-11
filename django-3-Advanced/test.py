class TelMixin:
	def telFunc(self):
		print (f'{self.name} can make calls')

class Phone(TelMixin):
	def __init__(self, name="iPhone"):
		self.name = name

def myfunc():
	moto = Phone()
	moto.telFunc()

def my_args(*args, **kwargs):
	print(args)
	print(kwargs)

if __name__ == "__main__":
	# myfunc()
	my_args(1,2,3,4,5, name='name', num=2)