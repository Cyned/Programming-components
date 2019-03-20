
input_str    = lambda *args, **kwargs: input(*args, **kwargs)
input_number = lambda *args, **kwargs: input(*args, **kwargs)
input_int = lambda *args, **kwargs: input(*args, **kwargs)
input_float = lambda *args, **kwargs: input(*args, **kwargs)


def get_service():
    params = {}
    name = input_str('Input new name:')
    params['new_name'] = str(name)
    frequency = input_float('Input new frequency:')
    params['new_frequency'] = float(frequency)
    hard_disk = input_int('Input new hard_disk:')
    params['new_hard_disk'] = int(hard_disk)
    ram = input_int('Input new ram:')
    params['new_ram'] = int(ram)
    cores = input_int('Input number of cores:')
    params['new_cores'] = int(cores)
    return params
