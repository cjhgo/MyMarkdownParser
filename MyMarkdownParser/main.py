#coding: utf-8
#created at 17-4-26 16:17
from itertools import takewhile


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

index = 0

def get_element(stream):
    global index
    while index < len(stream):
        while index < len(stream) and stream[index] == '\n':
            index += 1
        char = stream[index]
        if index == 0 or stream[index-1] == '\n':
            if char == '#':
                pos = index
                while stream[pos] == '#':
                    pos += 1

                level = pos - index
                index = pos
                while stream[pos] != '\n':
                    pos += 1

                content = stream[index: pos]

                index = pos+1
                return H(level=level, content=content)
            if char == '`':
                if stream[index: index+3] == "```" and stream[index+3] != "`":
                    pos = index+3
                    while stream[pos: pos+5] != "\n```\n":
                        pos += 1

                    content = stream[index+4: pos]

                    index = pos+5
                    return Pre(content)
            if char == '>':
                pos = index+1
                while stream[pos: pos+2] != '\n\n':
                    pos += 1

                content = stream[index+1: pos]
                index = pos
                return Quote(content)

stream = """# aa
## ddd

```
print
cout
log
alert
```

# ds
### dfsdfs

> i love you
aa

"""







while index < len(stream):
    E = get_element(stream)
    print E
