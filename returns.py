from functools import wraps as _wraps

__author__ = 'Michael'
__version__ = '1.0'


class returns(object):
    def __init__(self, type_, allow_none=False):
        self.__type = type_
        self.__allow_none = allow_none

    def __call__(self, func):
        @_wraps(func)
        def __new_func(*args, **kwargs):
            val = func(*args, **kwargs)
            if self.__allow_none and val is None:
                return None
            return self.__type(val)

        return __new_func
