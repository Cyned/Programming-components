from lab1 import Laptop


class Tablet(Laptop):

    def __init__(self, os_name, diagonal, battery_capacity, *args, **kwargs):
        self._os_name = os_name
        self._diagonal = diagonal
        self._battery = battery_capacity
        super(Tablet, self).__init__(*args, **kwargs)

    @property
    def os_name(self):
        """ Returns OS on this device """
        return self._os_name

    @property
    def diagonal(self):
        """ Returns diagonal of the screen"""
        return self._diagonal

    @property
    def battery(self):
        """ Returns the capacity of the battery """
        return self._battery

    def __str__(self):
        base_str = super(Tablet, self).__str__()
        params = dict(os_name=self.os_name, diagonal=self.diagonal, battery=self.battery, **base_str)
        return params
