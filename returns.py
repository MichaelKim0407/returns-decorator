from functools import wraps as _wraps

__author__ = 'Michael'
__version__ = '1.0'


class returns(object):
    def __init__(self, type_):
        self.__type = type_

    def __call__(self, func):
        @_wraps(func)
        def __new_func(*args, **kwargs):
            return self.__type(func(*args, **kwargs))

        return __new_func
