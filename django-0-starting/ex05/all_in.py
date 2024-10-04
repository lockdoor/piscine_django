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

# can find capital with key or value
def my_func():
	if len(sys.argv) != 2:
		return
	arg = sys.argv[1]

	key_words: list[str] = [key_word.strip() for key_word in arg.split(",") if len(key_word.strip())]
	states_keys :list[str] = [key.lower() for key in states.keys()]
	states_values: list[str] = [key.lower() for key in states.values()]
	capital_cities_keys :list[str] = [key.lower() for key in capital_cities.keys()]
	capital_cities_values :list[str] = [key.lower() for key in capital_cities.values()]
	
	def print_found(capital, state):
		print(f'{capital} is the captital of {state}')

	def print_not_found(key_word):
		print (f'{key_word} is neither a capital city nor a state')
	for key_word in key_words:
		# find in states.key
		try:
			if key_word.lower() in states_keys:
				index = states_keys.index(key_word.lower())
				state_key = list(states.keys())[index]
				print_found(capital_cities[states[state_key]], state_key)
			# find in capital_cities.key
			elif key_word.lower() in capital_cities_keys:
				index = states_values.index(key_word.lower())
				state_key = list(states.keys())[index]
				print_found(capital_cities[states[state_key]], state_key)
			# find in capital_cities.value
			elif key_word.lower() in capital_cities_values:
				index = capital_cities_values.index(key_word.lower())
				index = states_values.index(capital_cities_keys[index])
				state_key = list(states.keys())[index]
				print_found(capital_cities[states[state_key]], state_key)
			else:
				print_not_found(key_word)
		except ValueError as e:
			print_not_found(key_word)

if __name__ == '__main__':
	my_func()


'''
% python3 all_in.py "AL, Oregon, toto, , Salem, salem, oregon, al" 
Montgomery is the captital of Alabama
Salem is the captital of Oregon
toto is neither a capital city nor a state
Salem is the captital of Oregon
Salem is the captital of Oregon
Salem is the captital of Oregon
Montgomery is the captital of Alabama
'''