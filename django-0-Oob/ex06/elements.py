from elem import Text, Elem

class Html(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("html", attr=attr, content=content)

	def is_valid(self):
		try: 
			if len(self.content) != 2 \
				or not isinstance (self.content[0], Head) \
				or not isinstance (self.content[1], Body):
				raise Elem.ValidationError(self.tag)
			for elem in self.content:
				elem.is_valid()
			return True
		except IndexError:
			raise Elem.ValidationError(self.tag)
		except Elem.ValidationError:
			raise


class Head(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("head", attr=attr, content=content)
	
	def is_valid(self):
		title_count = 0
		try:
			for elem in self.content:
				elem.is_valid()
				if isinstance(elem, Title):
					title_count += 1
			if title_count == 1:
				return True
			raise Elem.ValidationError(self.tag)
		except Elem.ValidationError:
			raise

class Body(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("body", attr=attr, content=content)

	def is_valid(self):
		return True

class Title(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("title", attr=attr, content=content)

	def is_valid(self):
		print (f'{self.tag}.is_valid()')
		if not isinstance(self.content, Text):
			raise Elem.ValidationError(self.tag)
		return True


class Meta(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("meta", attr=attr, content=content, tag_type='simple')

class Img(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("img", attr=attr, content=content, tag_type='simple')

class Table(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("table", attr=attr, content=content)

class Th(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("th", attr=attr, content=content)

class Tr(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("tr", attr=attr, content=content)

class Td(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("td", attr=attr, content=content)

class Ul(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("ul", attr=attr, content=content)

class ol(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("ol", attr=attr, content=content)

class Li(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("li", attr=attr, content=content)

class H1(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("h1", attr=attr, content=content)

class H2(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("h1", attr=attr, content=content)

class P(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("p", attr=attr, content=content)

class Div(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("div", attr=attr, content=content)

class Span(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("span", attr=attr, content=content)

class Hr(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("hr", attr=attr, content=content, tag_type='simple')

class Br(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("br", attr=attr, content=content, tag_type='simple')

def my_test():
	print(Html(
		[
			Head([
				Meta(attr={'charset': 'UTF8'}), 
				Title(Text("'hello my page'"))
				]), 
			Body([
				Img(attr={'src': "http://i.imgur.com/pfp3T.jpg"}),
				Ul([
					Li(Text('dog')), 
					Li(Text('cat')), 
					Li(Text('fish'))
					]),
				H1(Text("'oh my god'")),
				Table([
					Tr([
						Th(Text('th1')), 
						Td(Text('td1'))
						]),
					Tr([
						Th(Text('th2')), 
						Td(Text('td2'))
						]),					
					]),
				Br(),
			])
		]))

if __name__ == '__main__':
	my_test()