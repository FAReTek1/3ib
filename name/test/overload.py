from functools import singledispatch, singledispatchmethod

class Temp:
    @singledispatchmethod
    # this is used since singledispatch cannot be uised inside classes
    def subtrac(self, a, b):
        raise NotImplementedError("idek")

    @subtrac.register
    def _(self, a: str, b,):
        return f"{self.__dict__} {a} {b}"

@singledispatch
def add(a, b):
    raise NotImplementedError("idek")


@add.register
def _(a: float, b: int):
    print(a + b, ", hm!")


print(add(1.7, 3.14))
