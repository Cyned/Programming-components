from time import sleep

from typing import List
from lab6.patterns.command import Invoker, ConcreteCommand
from lab6.patterns.proxy import ProxyLaptop


class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


def requires_permission(permission: str):
    """
    Decorator that add permission requirements
    :param permission: name of permission
    """
    def decorator(fn):
        def decorated(*args, **kwargs):
            permissions = get_permissions(current_user_id())
            if permission in permissions:
                return fn(*args, **kwargs)
            raise Exception("permission denied")

        return decorated

    return decorator


def get_permissions(user_id):
    if user_id == 1:
        return ['logging_in', ]
    return []


def current_user_id():
    return 1


class Laptop(object, metaclass=Singleton):

    def __init__(self, name: str, n_ports: int = 3):
        self.name: str = name
        self.__switched_on: bool = False

        self._usb_ports: List = [False] * n_ports

        self.counter: int = -1  # for iteration about the usb ports

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        """ Iterate about projects """
        self.counter += 1
        if self.counter < len(self.usb_ports):
            return self.usb_ports[self.counter]
        raise StopIteration

    @property
    def usb_ports(self):
        """ Returns usb ports """
        return self._usb_ports

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

    @requires_permission('logging_in')
    def turn_on(self):
        """ Turn on the Laptop """
        if not self.switched_on:
            print('Laptop is turning on...')
            self.__switched_on = True
        else:
            print('Laptop is already switched on.')

    def get_user(self):
        """ Print user logged in """
        return 'denis'
