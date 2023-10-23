import math
from typing import Iterable
# Fail: see const rev 2

class ReadOnlyError(Exception):
    pass


class Const:
    def __init__(self, value):
        self.__dict__["value"] = value

    def __setitem__(self, key, value):
        raise ReadOnlyError("Constant values cannot be changed")

    def __repr__(self):
        return f'Const({self.__dict__["value"].__repr__()})'

    def __str__(self):
        return self.__dict__["value"].__str__()

    def __bytes__(self):
        return self.__dict__["value"].__bytes__()

    def __format__(self, format_spec):
        return self.__dict__["value"].__format__(format_spec)

    def __lt__(self, other):
        return self.__dict__["value"].__lt__(other)

    def __eq__(self, other):
        return self.__dict__["value"].__eq__(other)

    def __ne__(self, other):
        return self.__dict__["value"].__ne__(other)

    def __gt__(self, other):
        return self.__dict__["value"].__gt__(other)

    def __ge__(self, other):
        return self.__dict__["value"].__ge__(other)

    def __hash__(self):
        return self.__dict__["value"].__hash__()

    def __bool__(self):
        return self.__dict__["value"].__bool()

    def __getattr__(self, item):
        return self.__dict__["value"].__getattr__(item)

    def __getattribute__(self, item):
        if item == "__dict__":
            return object.__getattribute__(self, item)
        return self.__dict__["value"].__getattribute__(item)

    def __setattr__(self, key, value):
        raise ReadOnlyError("Constant values cannot be changed")

    def __delattr__(self, item):
        self.__dict__["value"].__delattr__(item)

    def __dir__(self) -> Iterable[str]:
        return self.__dict__["value"].__dir__()

    def __get__(self, instance, owner):
        return self.__dict__["value"].__get__(instance, owner)

    def __set__(self, instance, value):
        raise ReadOnlyError("Constant values cannot be changed")

    def __delete__(self, instance):
        self.__dict__["value"].__delete__(instance)

    def __init_subclass__(cls, **kwargs):
        cls.__dict__["value"].__init_subclass__(kwargs=kwargs)

    def __set_name__(self, owner, name):
        self.__dict__["value"].__set_name__(owner, name)

    def __instancecheck__(self, instance):
        return self.__dict__["value"].__instancecheck__(instance)

    def __subclasscheck__(self, subclass):
        return self.__dict__["value"].__subclasscheck__(subclass)

    def __class_getitem__(cls, item):
        cls.__dict__["value"].__class_getitem__(item)

    def __call__(self, *args, **kwargs):
        self.__dict__["value"].__call__(args=args, kwargs=kwargs)

    def __len__(self):
        return self.__dict__["value"].__len__()

    def __length_hint__(self):
        return self.__dict__["value"].__length_hint__()

    def __getitem__(self, item):
        return self.__dict__["value"].__getitem__(item)

    def __delitem__(self, key):
        self.__dict__["value"].__delitem__(key)

    def __missing__(self, key):
        return self.__dict__["value"].__missing__(key)

    def __iter__(self):
        return self.__dict__["value"].__iter__()

    def __reversed__(self):
        return self.__dict__["value"].__reversed__()

    def __contains__(self, item):
        return self.__dict__["value"].__contains__(item)

    def __add__(self, other):
        return self.__dict__["value"].__add__(other)

    def __radd__(self, other):
        return self.__dict__["value"].__radd__(other)

    def __iadd__(self, other):
        raise ReadOnlyError("Constant values cannot be changed")

    def __sub__(self, other):
        return self.__dict__["value"].__sub__(other)

    def __mul__(self, other):
        return self.__dict__["value"].__mul__(other)

    def __matmul__(self, other):
        return self.__dict__["value"].__matmul__(other)

    def __truediv__(self, other):
        return self.__dict__["value"].__truediv__(other)

    def __floordiv__(self, other):
        return self.__dict__["value"].__floordiv__(other)

    def __mod__(self, other):
        return self.__dict__["value"].__mod__(other)

    def __divmod__(self, other):
        return self.__dict__["value"].__divmod__(other)

    def __pow__(self, power, modulo=None):
        return self.__dict__["value"].__pow__(power, modulo)

    def __lshift__(self, other):
        return self.__dict__["value"].__lshift__(other)

    def __rshift__(self, other):
        return self.__dict__["value"].__rshift__(other)

    def __and__(self, other):
        return self.__dict__["value"].__and__(other)

    def __xor__(self, other):
        return self.__dict__["value"].__xor__(other)

    def __or__(self, other):
        return self.__dict__["value"].__or__(other)


pi = Const(math.pi)

print(pi)
pi = 22
print(pi)

# Not all dunders are implemented...
# https://mathspp.com/blog/pydonts/dunder-methods
