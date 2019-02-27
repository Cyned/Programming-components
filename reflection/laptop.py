import json
from time import sleep

from reflection import reflect_methods, reflect_attrs, reflect_subclasses


class Laptop(object):

    _a = 'Hi'

    def __init__(self, *, name: str, frequency: float, core_number: int, ram: int, hard_disk: int):
        self._name        = name
        self._frequency   = frequency
        self._core_number = core_number
        self._ram         = ram
        self._hard_disk   = hard_disk

    @property
    def name(self) -> str:
        """ Returns name """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Set the new name
        :param name: new name
        """
        if name:
            self._name = name

    @property
    def frequency(self) -> float:
        """ Returns frequency """
        return self._frequency

    @property
    def core_number(self) -> int:
        """ Returns cores number """
        return self._core_number

    @property
    def ram(self) -> int:
        """ Returns RAM """
        return self._ram

    @property
    def hard_disk(self) -> int:
        """ Returns hard disk capacity """
        return self._hard_disk

    def turn_off(self, time: int = 5):
        """
        Turn off the Laptop after `time` seconds
        :param time: time in seconds
        """
        time = min(time, 5)
        print(f'Laptop will turn off in {time} seconds.')
        sleep(time)
        print('Laptop is turning off...')

    def __str__(self) -> str:
        params = {'name': self.name, 'frequency': self.frequency, 'ram': self.ram, 'hard_disk': self.hard_disk}
        return json.dumps(params)


if __name__ == '__main__':
    global_dict = globals()
    print(global_dict)
    obj = global_dict['Laptop'](
        name='Lenovo', frequency=1.2, core_number=2, ram=4, hard_disk=64,
    )
    print('-' * 10)
    reflect_methods(global_dict['Laptop'])
    print('-' * 10)
    reflect_attrs(global_dict['Laptop'])
    print('-' * 10)
    reflect_subclasses(global_dict['Laptop'])
