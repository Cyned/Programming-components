import numpy as np


class TypeDefaults_class(object):

    @property
    def __array(self):
        return (np.random.randint(1, 100) for _ in range(10))

    @property
    def int(self): return np.random.randint(1, 100)

    @property
    def float(self): return np.random.random() * 100

    @property
    def bool(self): return np.random.choice([True, False])

    @property
    def str(self): return 'String'

    @property
    def list(self): return list(self.__array)

    @property
    def tuple(self): return tuple(self.__array)

    @property
    def set(self): return set(self.__array)

    @property
    def frozenset(self): return frozenset(self.__array)

    @property
    def dict(self): return dict(zip(tuple(self.__array), tuple(self.__array)))

    @property
    def NoneType(self): return None

    def get(self, item):
        return getattr(self, item.__name__)


TypeDefaults = TypeDefaults_class()


def reflect_methods(obj):
    """
    Reflect the object`s methods
    :param obj: object that have to be reflected
    """
    print(f'Reflect methods `{obj}`')
    instance, _ = get_instance(obj=obj)
    for item in [i for i in dir(obj) if not i.startswith('_')]:
        func = getattr(instance, item)
        if callable(func) and func.__annotations__:
            params = {key: TypeDefaults.get(value) for key, value in func.__annotations__.items() if key is not 'return'}
            result = func(**params)
            print(f'Method `{func.__code__.co_name} ({params})`: {result}')


def reflect_attrs(obj):
    """
    Reflect the object`s attributes
    :param obj: object that have to be reflected
    """
    print(f'Reflect attributes `{obj}`')
    instance, annotations = get_instance(obj=obj)
    for item in [i for i in dir(instance) if not i.startswith('_')]:
        func = getattr(instance, item)
        if not callable(func) and item in annotations:
            print(f'Attribute `{item}`:{annotations[item].__name__} <--> {func}:{type(func).__name__}')


def get_instance(obj):
    annotations = {}
    params = {}
    for key, value in obj.__init__.__annotations__.items():
        params[key] = TypeDefaults.get(value)
        annotations[key] = value
    if obj.__base__ is not object:
        for key, value in obj.__base__.__init__.__annotations__.items():
            params[key] = TypeDefaults.get(value)
            annotations[key] = value
    return obj(**params), annotations


def reflect_subclasses(obj):
    """
    Reflect the object`s subclasses
    :param obj: object that have to be reflected
    """
    print(f'Reflect subclasses `{obj}`')
    subclasses = obj.__subclasses__()
    print(f'Subclasses of `{obj}` is {set(subclasses)}')


if __name__ == '__main__':
    class A(object):
        a = 1

        def func(self, a: int) -> str:
            print(f'a: {a}')
            return 'Hello, here I am'

    reflect_methods(A())
    reflect_attrs(A())
    reflect_subclasses(A)
