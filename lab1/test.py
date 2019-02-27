from lab1 import Laptop, Tablet
from lab1.reflection import reflect_attrs, reflect_subclasses, reflect_methods


if __name__ == '__main__':
    laptop = Laptop(
        name='Lenovo', frequency=1.2, core_number=4, ram=8, hard_disk=256,
    )
    print(f'Laptop: {laptop}')

    tablet = Tablet(
        os_name='Android', diagonal=16.5, battery=10000,
        name='Lenovo', frequency=1.2, core_number=2, ram=4, hard_disk=64,
    )
    print(f'Tablet: {tablet}')

    print('-' * 10)
    reflect_methods(Tablet)
    print('-' * 10)
    reflect_attrs(Tablet)
    print('-' * 10)
    reflect_subclasses(Laptop)
