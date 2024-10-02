import sys

states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
}
capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
}

def my_func():
	if len(sys.argv) != 2:
		return
	arg = sys.argv[1]
	# for city in capital_cities:
	# 	if capital_cities[city] == arg:
	# 		for stage in states:
	# 			if states[stage] == city:
	# 				return print(stage)
	try:
		idx = list(capital_cities.values()).index(arg)
		city = list(capital_cities.keys())[idx]
		idx = list(states.values()).index(city)
		print(list(states.keys())[idx])
	except ValueError:
		print('Unknown capital city')

if __name__ == '__main__':
	my_func()
