import time


class LoadTimeMeta(type):
    load_start_time = time.perf_counter()

    def __new__(mcs, name, bases, namespace):
        print(mcs, name, bases, namespace)
        namespace["__class_load_time__"] = time.perf_counter() - LoadTimeMeta.load_start_time
        return super().__new__(mcs, name, bases, namespace)


class Foo(metaclass=LoadTimeMeta):
    pass


a = Foo()
print(f"{a.__class_load_time__=}")
