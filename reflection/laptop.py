import json
from time import sleep

from reflection.reflection import reflect_methods, reflect_attrs, reflect_subclasses


class Laptop(object):

    _frequency   = None
    _core_number = None
    _ram         = None
    _hard_disk   = None

    def __init__(self, *, name: str, frequency: float, core_number: int, ram: int, hard_disk: int):
        self.name        = name
        self.frequency   = frequency
        self.core_number = core_number
        self.ram         = ram
        self.hard_disk   = hard_disk

        self.__switched_on = False

    @property
    def name(self) -> str:
        """ Returns name """
        return self._name

    @name.setter
    def name(self, name: str):
        """ Set the new name """
        if name:
            self._name = name

    @property
    def frequency(self) -> float:
        """ Returns frequency """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency: float):
        """ Set frequency """
        if isinstance(frequency, float) and frequency > 0:
            self._frequency = frequency

    @property
    def core_number(self) -> int:
        """ Returns cores number """
        return self._core_number

    @core_number.setter
    def core_number(self, cores):
        """ Set cores number """
        if isinstance(cores, int) and cores > 0:
            self._core_number = cores

    @property
    def ram(self) -> int:
        """ Returns RAM """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """ Set RAM """
        if isinstance(ram, int) and ram > 0:
            self._ram = ram

    @property
    def hard_disk(self) -> int:
        """ Returns hard disk capacity """
        return self._hard_disk

    @hard_disk.setter
    def hard_disk(self, hard_disk):
        """ Returns hard disk capacity """
        if isinstance(hard_disk, int) and hard_disk > 0:
            self._hard_disk = hard_disk

    @property
    def switched_on(self):
        """ Return if the Laptop is switched on """
        return self.__switched_on

    def turn_off(self, time: int = 5):
        """
        Turn off the Laptop after `time` seconds
        :param time: time in seconds
        """
        if self.switched_on:
            time = min(time, 5)
            print(f'Laptop will turn off in {time} seconds.')
            sleep(time)
            print('Laptop is turning off...')
            self.__switched_on = False
        else:
            print('Laptop is already switched off.')

    def turn_on(self):
        """ Turn on the Laptop """
        if not self.switched_on:
            print('Laptop is turning on...')
            self.__switched_on = True
        else:
            print('Laptop is already switched on.')

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
