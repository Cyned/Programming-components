import json

from reflection import Laptop
from reflection.reflections import reflect_attrs, reflect_methods, reflect_subclasses


class Tablet(Laptop):

    _os_name:  str   = None
    _diagonal: float = None
    _battery:  int   = None

    def __init__(self, *, os_name: str, diagonal: float, battery: int, **kwargs):
        super(Tablet, self).__init__(**kwargs)
        self.os_name = os_name
        self.diagonal = diagonal
        self.battery = battery

    @property
    def os_name(self) -> str:
        """ Returns OS on this device """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """ Set new operating system value """
        if not os_name or not isinstance(os_name, str):
            raise TypeError
        self._os_name = os_name

    @property
    def diagonal(self) -> float:
        """ Returns diagonal of the screen"""
        return self._diagonal

    @diagonal.setter
    def diagonal(self, diagonal):
        """ Set new diagonal """
        if not isinstance(diagonal, float) or diagonal <= 0:
            raise TypeError
        self._diagonal = diagonal

    @property
    def battery(self) -> int:
        """ Returns the capacity of the battery """
        return self._battery

    @battery.setter
    def battery(self, battery):
        """ Set new battery capacity value """
        if not isinstance(battery, int) or battery <= 0:
            raise TypeError
        self._battery = battery

    def __str__(self) -> str:
        base_str = json.loads(super(Tablet, self).__str__())
        params = dict(os_name=self.os_name, diagonal=self.diagonal, battery=self.battery, **base_str)
        return json.dumps(params)


if __name__ == '__main__':
    global_dict = globals()
    print(global_dict)
    obj = global_dict['Tablet'](
        os_name='Android', diagonal=15.3, battery=10000,
        name='Lenovo', frequency=1.2, core_number=2, ram=4, hard_disk=64,
    )
    print('-' * 10)
    reflect_methods(global_dict['Tablet'])
    print('-' * 10)
    reflect_attrs(global_dict['Tablet'])
    print('-' * 10)
    reflect_subclasses(global_dict['Laptop'])
