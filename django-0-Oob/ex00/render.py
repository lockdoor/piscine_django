import settings
import sys
import re

def my_func():
	if len(sys.argv) != 2:
		print("Wrong argument", file=sys.stderr)
		return 1
	try:
		file = open(sys.argv[1], 'r')
		result = ""
		for line in file:
			line = re.sub(r"\{\s*name\s*\}", settings.name, line)
			line = re.sub(r"\{\s*sername\s*\}", settings.sername, line)
			line = re.sub(r"\{\s*age\s*\}", settings.age, line)
			line = re.sub(r"\{\s*profession\s*\}", settings.profession, line)
			result += line
		file.close()
		file = open('file.html', 'w')
		file.write(result)
		file.close()
	except FileNotFoundError:
		print(f'File {sys.argv[1]} not found', sys.stderr)
		return 1

if __name__ == '__main__':
	my_func()
