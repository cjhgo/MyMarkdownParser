#coding: utf-8
#created at 17-5-31 11:07


class Element(object):
    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        return self._content.replace("\n", "<br>")

    def __repr__(self):
        return self.output()

    def output(self):
        return self.content

class Text(Element):
    def output(self):
        return "<p>{0}</p>".format(self.content)

class H(Element):
    level = 0
    def __init__(self, level, content):
        self.level = level
        self.token = "#"*self.level
        self.tag = "h"+str(self.level)
        self._content = content


    def output(self):
        return "<{0}>{1}</{0}".format(self.tag, self.content)


class Pre(Element):
    def output(self):
        return "<pre>{0}</pre>".format(self.content)


class Quote(Element):
    pass


class EOF(Element):
    pass


class Blank(Element):
    content = "<br>"
