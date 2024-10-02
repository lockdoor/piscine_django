def my_func():
	file = open('numbers.txt', 'r')
	str = file.read()
	file.close()
	numbers: list[int] = [int(ele) for ele in str.split(',')]
	for el in numbers:
		print(el)

if __name__ == '__main__':
	my_func()