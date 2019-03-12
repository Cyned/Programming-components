from mocki.controller import Controller


input_str    = lambda *args, **kwargs: input(*args, **kwargs)
input_number = lambda *args, **kwargs: input(*args, **kwargs)


def get_service():
    controller = Controller()
    name = input_str('Input new name:')
    controller.set_name(new_name=name)
    frequency = input_number('Input new frequency:')
    controller.set_frequency(new_frequency=frequency)
    hard_disk = input_number('Input new hard_disk:')
    controller.set_hard_disk(new_hard_disk=hard_disk)
    ram = input_number('Input new ram:')
    controller.set_ram(new_ram=ram)
    return controller
