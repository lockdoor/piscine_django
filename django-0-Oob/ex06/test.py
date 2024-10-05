from elements import *
class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__()
        # self.content = content or []
        self.add_content(content)

    def is_valid(self):
        try: 
            if not isinstance(self.content[0], Head) or not isinstance(self.content[1], Body):
                raise Elem.ValidationError(self)
            # for elem in self.add_content:
            #     if not elem.is_valid():
            #         return False
            return True
        except IndexError:
            raise Elem.ValidationError(self)
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
if __name__ == '__main__':
    html_instance = Html(content=[Head()])
    page = Page(elem=html_instance)

    if page.is_valid():
        print("Page is valid")
    else:
        print("Page is not valid")
