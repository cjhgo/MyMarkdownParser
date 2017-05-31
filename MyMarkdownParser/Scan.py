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
        else:
            begin = self.index
            while True:
                while self.peek != "\n":
                    self.advance()
                self.advance()
                if self.peek in ("\n", '`', '#'):
                    break
            end = self.index
            return Text(self.stream[begin:end])
if __name__ == "__main__":
    stream ="""## note1984\n修改结果能否互相影响(看见)
python返回list修改能否看见
cpp.返回指向同一个地址的指针,则修改能看见

对象分布在内存中,是带有状态的
函数每次调用都是重新执行一次,无法记录状态

python中的函数闭包是带有状态的函数

```
def returnlist():
    x = [1,2,3]
    def foo():
        return x
    return foo
    ff = returnlist()
```\n
"""
    print stream
    scan = Scan(stream)
    t = scan.scan()
    print t

    while not isinstance(t, EOF):
        t = scan.scan()
        print t
