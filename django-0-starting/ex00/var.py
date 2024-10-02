def my_print(arg):
	print(f'{arg} has at type {type(arg)}')

def my_var():
	var = 42
	my_print(var)
	var = '42'
	my_print(var)
	var = 'quarante-deux'
	my_print(var)
	var = 42.0
	my_print(var)
	var = True
	my_print(var)
	var = [42]
	my_print(var)
	var = {42: 42}
	my_print(var)
	var = (42,)
	my_print(var)
	var = set()
	my_print(var)

if __name__ == '__main__':
	my_var()