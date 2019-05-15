from time import sleep


class BaseLaptop(object):

    def __init__(self, name: str):
        self.name: str = name
        self.__switched_on: bool = False

    @property
    def name(self) -> str:
        """ Returns name """
        return self._name

    @name.setter
    def name(self, name: str):
        """ Set the new name """
        if not name or not isinstance(name, str):
            raise TypeError
        self._name = name

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


class Lenovo(BaseLaptop):
    @classmethod
    def is_model_for(cls, model: str) -> bool:
        return model.lower() == 'lenovo'


class Acer(BaseLaptop):
    @classmethod
    def is_model_for(cls, model: str) -> bool:
        return model.lower() == 'acer'


def Laptop(model):
    for cls in BaseLaptop.__subclasses__():
        if cls.is_model_for(model=model):
            return cls(model)
    raise ValueError


if __name__ == '__main__':
    print(Laptop('lenovo'))
    print(Laptop('acer'))
