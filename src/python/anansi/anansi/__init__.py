import typing as t
from dis import disassemble

def disit(func):
    def dissed():


class DictLoader:

    @disit
    def __init__(self, colors: t.Dict[str,str] = {}):
        if colors:
            self.from_kwargs(colors=colors)

    def from_kwargs(self, **colors):
        # obj = cls()
        for name, code in colors.items():
            # print(name, ': ', code)
            setattr(self, name, code)
        # return obj

test_colors = {
    'Blue': 'Blue',
    'Red': 'Red',
    'Green': 'Green',
}

d = DictLoader(colors=test_colors)

print(dir(d))
print(d.colors)
