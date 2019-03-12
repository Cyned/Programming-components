
from reflection.laptop import Laptop
from mocki.view import View


class Controller(object):

    def __init__(self, name='Lenovo', frequency=1.2, core_number=2, ram=4, hard_disk=64):
        super(Controller, self).__init__()
        self.__laptop = Laptop(
            name=name, frequency=frequency, core_number=core_number, ram=ram, hard_disk=hard_disk,
        )
        self.__view = View(self.laptop)

    def set_name(self, new_name):
        """ Set new name """
        self.laptop.name = str(new_name)

    def get_name(self):
        """ Returns core number """
        return self.laptop.name

    def set_frequency(self, new_frequency):
        """ Set new frequency"""
        self.laptop.frequency = float(new_frequency)

    def get_frequency(self):
        """ Returns frequency """
        return self.laptop.frequency

    def set_cores(self, new_cores):
        """ Set new core number """
        self.laptop.core_number = int(new_cores)

    def get_cores(self):
        """ Returns core number """
        return self.laptop.core_number

    def set_ram(self, new_ram):
        """ Set new ram """
        self.laptop.ram = int(new_ram)

    def get_ram(self):
        """ Returns ram """
        return self.laptop.ram

    def set_hard_disk(self, new_hard_disk):
        """ Set new hard disk """
        self.laptop.hard_disk = int(new_hard_disk)

    def get_hard_disk(self):
        """ Returns hard disk """
        return self.laptop.hard_disk

    def update_view(self):
        """ Update params of the View class """
        self.view.name      = self.laptop.name
        self.view.frequency = self.laptop.frequency
        self.view.hard_disk = self.laptop.hard_disk
        self.view.ram       = self.laptop.ram

    def print_details(self):
        """ Print details fro View class """
        self.view.print_details()

    @property
    def laptop(self):
        """ Returns laptop object """
        return self.__laptop

    @property
    def view(self):
        """ Returns View instance """
        return self.__view
