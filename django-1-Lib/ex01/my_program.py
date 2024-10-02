from path import Path

d = Path(".")

file = open(".log", 'w')
for f in d.files('*'):
	print (f, file=file)

my_dir = Path("my_dir").mkdir_p(mode=0o777)
log =  Path("my_dir/my_file").touch()
