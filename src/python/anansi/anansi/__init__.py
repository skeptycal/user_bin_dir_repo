# import typing as t
from dis import dis
from functools import wraps


def disit(func):
    """ Decorator for disassembly of code. """
    @wraps(func)
    def dissed():
        dis(func)
        retval = func()
        return retval
    return dissed


class DictLoader(dict):

    def __init__(self,  dict_colors={}):
        dict.__init__(self)
        if dict_colors:
            self.from_kwargs(dict_colors)

    def from_kwargs(self, dict_colors):
        # obj = cls()
        for name, code in dict_colors.items():
            # print(name, ': ', code)
            setattr(self, name, code)
        # return obj


if __name__ == '__main__':
    test_colors = {
        'Blue': 'BlueValue',
        'Red': 'RedValue',
        'Green': 'GreenValue',
    }

    print(test_colors)

    d = DictLoader(dict_colors=test_colors)

    # print(dir(d))
    print(d.Blue)
