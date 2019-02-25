

class Laptop(object):

    def __init__(self, *, name, frequency, core_number, ram, hard_disk):
        self._name        = name
        self._frequency   = frequency
        self._core_number = core_number
        self._ram         = ram
        self._hard_disk   = hard_disk

    @property
    def name(self):
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
    def frequency(self):
        """ Returns frequency """
        return self._frequency

    @property
    def core_number(self):
        """ Returns cores number """
        return self._core_number

    @property
    def ram(self):
        """ Returns RAM """
        return self._ram

    @property
    def hard_disk(self):
        """ Returns hard disk capacity """
        return self._hard_disk

    def __str__(self):
        params = {'name': self.name, 'frequency': self.frequency, 'ram': self.ram, 'hard_disk': self.hard_disk}
        return params
