import json


class View(object):

    def __init__(self, obj):
        super(View, self).__init__()
        self.name = obj.name
        self.frequency = obj.frequency
        self.ram = obj.ram
        self.hard_disk = obj.hard_disk

    def print_details(self):
        print(self)

    def __str__(self) -> str:
        params = {'name': self.name, 'frequency': self.frequency, 'ram': self.ram, 'hard_disk': self.hard_disk}
        return 'Laptop:\n' + json.dumps(params)
