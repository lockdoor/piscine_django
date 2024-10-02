d = [
('Hendrix', '1942'),
('Allman', '1946'),
('King', '1925'),
('Clapton', '1945'),
('Johnson', '1911'),
('Berry', '1926'),
('Vaughan', '1954'),
('Cooder', '1947'),
('Page', '1944'),
('Richards', '1943'),
('Hammett', '1962'),
('Cobain', '1967'),
('Garcia', '1942'),
('Beck', '1944'),
('Santana', '1947'),
('Ramone', '1948'),
('White', '1975'),
('Frusciante', '1970'),
('Thompson', '1949'),
('Burton', '1939')
]

def my_func():
	my_dict :dict[str] = {}
	for el in d:
		my_dict[int(el[1])] = el[0]
	for el in my_dict:
		print (f'{el} : {my_dict[el]}')

if __name__ == '__main__':
	my_func()
