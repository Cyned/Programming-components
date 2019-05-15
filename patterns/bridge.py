import abc

from time import sleep


class Abstraction:
    """
    Define the abstraction's interface.
    Maintain a reference to an object of type Laptop.
    """

    def __init__(self, imp):
        self._imp = imp

    def operation_on(self):
        self._imp.turn_on()

    def operation_off(self):
        self._imp.turn_off()


class Laptop(object):

    def __init__(self, name: str):
        self.name: str = name
        self._switched_on: bool = False

    @property
    def switched_on(self):
        """ Return if the Laptop is switched on """
        return self._switched_on

    @abc.abstractmethod
    def turn_off(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def turn_on(self, *args, **kwargs):
        pass


class Lenovo(Laptop):
    def turn_on(self):
        """ Turn on the Laptop """
        if not self.switched_on:
            print('Laptop is turning on...')
            self._switched_on = True
        else:
            print('Laptop is already switched on.')

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
            self._switched_on = False
        else:
            print('Laptop is already switched off.')


class Acer(Laptop):
    def turn_on(self):
        """ Turn on the Laptop """
        if not self.switched_on:
            print('Laptop is turning on...')
            self._switched_on = True
        else:
            print('Laptop is already switched on.')

    def turn_off(self):
        """
        Turn off the Laptop after `time` seconds
        """
        if self.switched_on:
            print(f'Laptop will turn off in 1 seconds.')
            sleep(1)
            print('Laptop is turning off...')
            self._switched_on = False
        else:
            print('Laptop is already switched off.')


if __name__ == "__main__":
    lenovo = Lenovo('lenovo')
    abstraction = Abstraction(lenovo)
    abstraction.operation_on()
    abstraction.operation_off()
