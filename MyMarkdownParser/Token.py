#coding: utf-8
#created at 17-5-31 11:07


class Element(object):
    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return self.content

class Text(Element):
    pass


class H(Element):
    level = 0
    def __init__(self, level, content):
        self.level = level
        self.token = "#"*self.level
        self.tag = "h"+str(self.level)
        self.content = content

    def __repr__(self):
        return self.output()

    def output(self):
        return "<{0}>{1}</{0}".format(self.tag, self.content)


class Pre(Element):
    pass


class Quote(Element):
    pass


class EOF(Element):
    pass


class Blank(Element):
    content = "<br>"
