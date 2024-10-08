from local_lib.path import Path

def my_func():
	my_dir = Path("my_dir").mkdir_p(mode=0o777)
	my_file =  Path(f"{my_dir}/my_file").touch()
	file = open(my_file, 'w')
	file.write("something in this file")
	file.close()
	file = open(my_file, 'r')
	print(file.read())

if __name__ == "__main__":
	my_func()