from elem import Text, Elem
from elements import *

class Page():
	def __init__(self, elem: Elem):
		self.elem = elem
	
	def is_valid(self):
		try:
			if not isinstance(self.elem, Html):
				return False
			return self.elem.is_valid()
		except Exception as e:
			print (e)
			return False

	class ValidationError(Exception):
		def __init__(self, msg: str):
			super().__init__("ValidationError on " + msg)


def test_not_html_at_first():
	head = Head()
	page = Page(head)
	if page.is_valid() == False:		
		print ("test_not_html_at_first Pass")
	else:
		raise Page.ValidationError("test_not_html_at_first")

def test_html_head_body():
	html = Html([Head([Title(Text("hello world"))]), Body()])
	page = Page(html)
	if page.is_valid() == True:
		print ("test_html_head_body Pass")
	else:
		raise Page.ValidationError("test_html_head_body")

def my_func():
	try:
		test_not_html_at_first()
		test_html_head_body()
	except Page.ValidationError as e:
		print(e)

if __name__ == '__main__':
	my_func()