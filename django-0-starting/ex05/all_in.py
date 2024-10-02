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
	cities: list[str] = [city.strip() for city in arg.split(",") if len(city.strip())]
	capital: list[str] = [city.lower() for city in list(capital_cities.values())]
	for city in cities:
		try:
			idx = capital.index(city.lower())
			key = list(capital_cities.keys())[idx]
			idx = list(states.values()).index(key)
			print(f'{capital_cities[key]} is the captital of {list(states.keys())[idx]}')
		except ValueError:
			print (f'{city} is neither a capital city nor a state')
	pass

if __name__ == '__main__':
	my_func()


# "New jersey, Tren ton, NewJersey, Trenton, toto, , sAlem"