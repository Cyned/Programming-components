import json


class View(object):

    def __init__(self):
        super(View, self).__init__()
        self.name        = None
        self.frequency   = None
        self.core_number = None
        self.ram         = None
        self.hard_disk   = None

    def update(self, *, name=None, frequency=None, ram=None, hard_disk=None, core_number=None, **kwargs):
        if name:
            self.name = name
        if frequency:
            self.frequency = frequency
        if ram:
            self.ram = ram
        if hard_disk:
            self.hard_disk = hard_disk
        if self.core_number:
            self.core_number = core_number

    def print_details(self):
        print(self)

    def __str__(self) -> str:
        params = {'name': self.name, 'frequency': self.frequency,
                  'ram': self.ram, 'hard_disk': self.hard_disk,
                  'core_number': self.core_number,
                  }
        return 'Laptop:\n' + json.dumps(params)
