
from reflection.laptop import Laptop
from mocki.view import View
from mocki.service import get_service, input_str, input_number, input_int, input_float


class Controller(object):

    def __init__(self):
        super(Controller, self).__init__()
        self.__laptop = None
        self.__view = View()

    def create_laptop(self):
        """  """
        params = get_service()
        self.__laptop = Laptop(
            name=params['new_name'],
            frequency=params['new_frequency'],
            core_number=params['new_cores'],
            ram=params['new_ram'],
            hard_disk=params['new_hard_disk'],
        )
        self.__update_view(
            name=        self.laptop.name,
            frequency=   self.laptop.frequency,
            core_number= self.laptop.core_number,
            ram=         self.laptop.ram,
            hard_disk=   self.laptop.hard_disk
        )

    def update_name(self):
        new_name = input_str("Input new name")
        self.laptop.name = str(new_name)
        self.view.update(name=self.laptop.name)

    def update_ram(self):
        new_ram = input_int("Input new ram")
        self.laptop.ram = int(new_ram)
        self.view.update(name=self.laptop.name)

    def update_cores(self):
        new_cores = input_int("Input new cores")
        self.laptop.core_number = int(new_cores)

    def update_frequency(self):
        new_frequency = input_float("Input new frequency")
        self.laptop.frequency = float(new_frequency)
        self.view.update(frequency=self.laptop.frequency)

    def update_hard_disk(self):
        new_hard_disk = input_int("Input new hard_disk ")
        self.laptop.hard_disk = int(new_hard_disk)
        self.view.update(hard_disk=self.laptop.hard_disk)

    def __update_view(self, *, name=None, frequency=None, hard_disk=None, ram=None, **kwargs):
        """ Update params of the View class """
        self.view.update(
            name=name, frequency=frequency, hard_disk=hard_disk, ram= ram, **kwargs
        )

    def print_details(self):
        """ Print details fro View class """
        self.view.print_details()

    @property
    def laptop(self):
        """ Returns laptop object """
        return self.__laptop

    @laptop.setter
    def laptop(self, new_laptop):
        self.__laptop = new_laptop

    @property
    def view(self):
        """ Returns View instance """
        return self.__view


if __name__ == '__main__':
    controller = Controller()
    controller.create_laptop()
    controller.print_details()
