from elem import Text, Elem

class Html(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("html", attr=attr, content=content)



class Head(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("head", attr=attr, content=content)

	def is_valid(self):
		return True

class Body(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("body", attr=attr, content=content)
	
	def is_valid(self):
		return True

# class Title(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("title", attr=attr, content=content)

# class Meta(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("meta", attr=attr, content=content, tag_type='simple')

# class Img(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("img", attr=attr, content=content, tag_type='simple')

# class Table(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("table", attr=attr, content=content)

# class Th(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("th", attr=attr, content=content)

# class Tr(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("tr", attr=attr, content=content)

# class Td(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("td", attr=attr, content=content)

# class Ul(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("ul", attr=attr, content=content)

# class ol(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("ol", attr=attr, content=content)

# class Li(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("li", attr=attr, content=content)

# class H1(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("h1", attr=attr, content=content)

# class H2(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("h1", attr=attr, content=content)

# class P(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("p", attr=attr, content=content)

# class Div(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("div", attr=attr, content=content)

# class Span(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("span", attr=attr, content=content)

# class Hr(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("hr", attr=attr, content=content, tag_type='simple')

# class Br(Elem):
# 	def __init__(self, content=None, attr={}):
# 		super().__init__("br", attr=attr, content=content, tag_type='simple')

# def my_test():
# 	print(Html(
# 		[
# 			Head([
# 				Meta(attr={'charset': 'UTF8'}), 
# 				Title(Text("'hello my page'"))
# 				]), 
# 			Body([
# 				Img(attr={'src': "http://i.imgur.com/pfp3T.jpg"}),
# 				Ul([
# 					Li(Text('dog')), 
# 					Li(Text('cat')), 
# 					Li(Text('fish'))
# 					]),
# 				H1(Text("'oh my god'")),
# 				Table([
# 					Tr([
# 						Th(Text('th1')), 
# 						Td(Text('td1'))
# 						]),
# 					Tr([
# 						Th(Text('th2')), 
# 						Td(Text('td2'))
# 						]),					
# 					]),
# 				Br(),
# 			])
# 		]))

# if __name__ == '__main__':
# 	my_test()