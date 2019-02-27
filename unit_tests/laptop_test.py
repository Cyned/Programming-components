import unittest

from reflection import Laptop


def get_laptop(name='Lenovo', frequency=1.2, core_number=2, ram=4, hard_disk=64):
    return Laptop(
        name=name, frequency=frequency, core_number=core_number, ram=ram, hard_disk=hard_disk,
    )


class TestLaptop(unittest.TestCase):

    def name_init(self):
        test_name = 'Lenovo'
        lap = get_laptop(name=test_name)
        self.assertEqual(lap.name, test_name, 'Check the __init__ functionality.')

    def name_setter(self):
        lap = get_laptop(name='Lenovo')
        lap.name = ''
        self.assertEqual(lap.name, 'Lenovo', 'Check name setter.')
        lap.name = 'Acer'
        self.assertEqual(lap.name, 'Acer', 'Check name setter.')

    def frequency_init(self):
        test_frequency = 1.2
        lap = get_laptop(frequency=test_frequency)
        self.assertEqual(lap.frequency, test_frequency, 'Check the __init__ functionality.')

    def frequency_set_negative(self):
        lap = get_laptop(frequency=1.2)
        lap.frequency = -2
        self.assertEqual(lap.frequency, 1.2, 'Check frequency setter.')
        lap.frequency = 2.1
        self.assertEqual(lap.frequency, 2.1, 'Check frequency setter.')
        lap.frequency = 2
        self.assertEqual(lap.frequency, 2.1, 'Check frequency setter.')

    def core_number_init(self):
        test_core_number = 1.2
        lap = get_laptop(frequency=test_core_number)
        self.assertEqual(lap.frequency, test_core_number, 'Check the __init__ functionality.')

    def core_number_setter(self):
        lap = get_laptop(core_number=4)
        lap.core_number = -2
        self.assertEqual(lap.core_number, 4, 'Check core_number setter.')
        lap.core_number = 2
        self.assertEqual(lap.frequency, 2, 'Check core_number setter.')
        lap.frequency = 2.2
        self.assertEqual(lap.frequency, 2, 'Check core_number setter.')

    def ram_init(self):
        test_ram = 8
        lap = get_laptop(ram=test_ram)
        self.assertEqual(lap.ram, test_ram, 'Check the __init__ functionality.')

    def ram_setter(self):
        lap = get_laptop(ram=4)
        lap.ram = -2
        self.assertEqual(lap.ram, 4, 'Check ram setter.')
        lap.ram = 2
        self.assertEqual(lap.ram, 2, 'Check ram setter.')
        lap.ram = 2.2
        self.assertEqual(lap.ram, 2, 'Check ram setter.')

    def hard_disk_init(self):
        test_hard_disk = 512
        lap = get_laptop(hard_disk=test_hard_disk)
        self.assertEqual(lap.ram, test_hard_disk, 'Check the __init__ functionality.')

    def hard_disk_setter(self):
        lap = get_laptop(hard_disk=512)
        lap.hard_disk = -256
        self.assertEqual(lap.hard_disk, 512, 'Check hard_disk setter.')
        lap.hard_disk = 'dfdf'
        self.assertEqual(lap.hard_disk, 512, 'Check hard_disk setter.')
        lap.hard_disk = 1000
        self.assertEqual(lap.hard_disk, 1000, 'Check hard_disk setter.')

    def switch_on_off(self):
        lap = get_laptop()
        self.assertFalse(lap.switched_on, 'Check if the laptop is switched off after init.')
        lap.turn_on()
        self.assertTrue(lap.switched_on, 'Check if the laptop has been turned on.')
        lap.turn_on()
        self.assertTrue(lap.switched_on, 'Check if the laptop stay turned on.')
        lap.turn_off()
        self.assertFalse(lap.switched_on, 'Check if the laptop has been turned off.')
