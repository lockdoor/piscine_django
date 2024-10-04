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
	state = states.get(arg)
	if state is None:
		print('Unknown state')
	else:
		print(capital_cities[state])

if __name__ == '__main__':
	my_func()
