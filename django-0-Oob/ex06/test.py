# class Elem:
#     class ValidationError(Exception):
#         pass

# class Head(Elem):
#     pass

# class Body(Elem):
#     pass
from elements import *
class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__()
        self.content = content or []
        self.add_content = content or []

    def is_valid(self):
        try: 
            if not isinstance(self.content[0], Head) or not isinstance(self.content[1], Body):
                raise Elem.ValidationError
            # for elem in self.add_content:
            #     if not elem.is_valid():
            #         return False
            return True
        except IndexError:
            raise Elem.ValidationError
        except Elem.ValidationError:
            raise

class Page():
    def __init__(self, elem: Elem):
        self.elem = elem
    
    def is_valid(self):
        if not isinstance(self.elem, Html):
            return False
        print(type(self.elem))
        return self.elem.is_valid()

# Test
html_instance = Html(content=[Head()])
page = Page(elem=html_instance)

if page.is_valid():
    print("Page is valid")
else:
    print("Page is not valid")
