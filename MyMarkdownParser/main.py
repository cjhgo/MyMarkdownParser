#coding: utf-8
#created at 17-4-26 16:17
from itertools import takewhile


class Element(object):
    pass


class H(Element):
    level = 0
    def __init__(self, level, content):
        self.level = level
        self.token = "#"*self.level
        self.tag = "h"+str(self.level)
        self.content = content

    def output(self):
        return "<{0}>{1}</{0}".format(self.tag, self.content)


def get_element(stream):
    for line in stream:
        if line[0] == "#":
            hlevel = len(list(takewhile(lambda x: x == "#", line)))
            return H(hlevel, line[hlevel:])
        elif line[0] == "*":
            pass



