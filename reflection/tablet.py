import json

from lab1 import Laptop
from lab1.reflection import reflect_attrs, reflect_methods, reflect_subclasses


class Tablet(Laptop):

    def __init__(self, *, os_name: str, diagonal: float, battery: int, **kwargs):
        self._os_name = os_name
        self._diagonal = diagonal
        self._battery = battery
        super(Tablet, self).__init__(**kwargs)

    @property
    def os_name(self) -> str:
        """ Returns OS on this device """
        return self._os_name

    @property
    def diagonal(self) -> float:
        """ Returns diagonal of the screen"""
        return self._diagonal

    @property
    def battery(self) -> int:
        """ Returns the capacity of the battery """
        return self._battery

    def __str__(self) -> str:
        base_str = json.loads(super(Tablet, self).__str__())
        params = dict(os_name=self.os_name, diagonal=self.diagonal, battery=self.battery, **base_str)
        return json.dumps(params)


if __name__ == '__main__':
    global_dict = globals()
    print(global_dict)
    obj = global_dict['Tablet'](
        os_name='Android', diagonal=15.3, battery_capacity=10000,
        name='Lenovo', frequency=1.2, core_number=2, ram=4, hard_disk=64,
    )
    print('-' * 10)
    reflect_methods(global_dict['Tablet'])
    print('-' * 10)
    reflect_attrs(global_dict['Tablet'])
    print('-' * 10)
    reflect_subclasses(global_dict['Laptop'])
