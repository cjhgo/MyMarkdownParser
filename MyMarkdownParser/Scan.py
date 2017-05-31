#coding: utf-8
#created at 17-5-31 11:03

from Token import *

class Scan(object):

    def __init__(self, stream):
        self.index = 0
        self.stream = stream
        self.cnt = len(self.stream)

    def advance(self):
        if self.index == self.cnt:
            pass
        else:
            self.index += 1

    @property
    def peek(self):
        if self.index == self.cnt:
            return '\x00'
        else:
            return self.stream[self.index]

    def scan(self):
        if self.peek == '\x00':
            return EOF("EOF")
        elif self.peek == "\n":
            while self.peek == '\n':
                self.advance()
            self.advance()
            return Blank('blank')

        elif self.peek == '#':
            level = 1
            while self.peek == '#':
                self.advance()
                level += 1

            begin = self.index
            while self.peek != "\n":
                self.advance()
            end = self.index
            self.advance()
            return H(level=level, content=self.stream[begin:end])
        elif self.peek == '`':
            if self.stream[self.index: self.index+3] == "```":
                while self.peek != "\n":
                    self.advance()
                self.advance()
                begin = self.index

                while self.stream[self.index:self.index+5] != "\n```\n":
                    self.advance()
                content = self.stream[begin:self.index]
                self.index += 5
                return Pre(content)
if __name__ == "__main__":
    stream = "```abcd\ndef\n```\n# aaa\n#dsds#ds\n\n\n\n###jfdslkdfjs\n"
    print stream
    scan = Scan(stream)
    t = scan.scan()
    print t

    while not isinstance(t, EOF):
        t = scan.scan()
        print t
        # if scan.index >= scan.cnt:
        #     exit()
