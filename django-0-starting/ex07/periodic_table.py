import sys

#1 split by = for name
#2 second element split by ,
#3 split key, value by :

datas: dict = {}

def to_dict(line: str):
	list1 = [el.strip() for el in line.split('=')]
	# print (list1)

	list2 = [el.strip() for el in list1[1].split(',')]
	# print (list2)

	data = {}
	for el in list2:
		list3 = [v.strip() for v in el.split(':')]
		data[list3[0]]=list3[1]
	# print (data)

	datas[list1[0]] = data
	# print (datas)

def to_table():
	table: str = '<table>\n'
	for key in datas:
		table += '\t\t<tr>\n'
		table += '\t\t\t<td>\n' # style on this
		table += f'\t\t\t\t<h4>{key}</h4>\n'
		table += '\t\t\t\t<ul>\n'
		table += f'\t\t\t\t\t<li>No {datas[key]["number"]}</li>\n'
		table += f'\t\t\t\t\t<li>{datas[key]["small"]}</li>\n'
		table += f'\t\t\t\t\t<li>{datas[key]["molar"]}</li>\n'
		electrons: list = [int(el) for el in datas[key]['electron'].split(' ')]
		table += f'\t\t\t\t\t<li>{sum(electrons)} electron</li>\n'
		table += '\t\t\t\t</ul>\n\t\t\t</td>\n\t\t</tr>\n'
	table += '\t</table>\n'
	return table

def to_html():
	html:str = f'''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>periodic_table</title>
</head>
<body>
	{to_table()}
</body>
</html>'''
	return html

def my_func():
	if len(sys.argv) != 2:
		print("error argument require only filename", file=sys.stderr)
		return 1
	try:
		file = open('periodic_table.txt', 'r')

		# line: str = file.readline()
		# to_dict(line)

		for line in file:
			to_dict(line)
			# to_table()
		print (to_html())

		file.close()
		file = open("periodic_table.html", 'w')
		file.write(to_html())
		file.close()


	except FileNotFoundError:
		return print("File not found")

if __name__ == '__main__':
	my_func()