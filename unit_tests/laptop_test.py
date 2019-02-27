import unittest

from reflection import Laptop


def get_laptop(name='Lenovo', frequency=1.2, core_number=2, ram=4, hard_disk=64):
    return Laptop(
        name=name, frequency=frequency, core_number=core_number, ram=ram, hard_disk=hard_disk,
    )


class TestLaptop(unittest.TestCase):

    def test_name_init(self):
        test_name = 'Lenovo'
        lap = get_laptop(name=test_name)
        self.assertEqual(lap.name, test_name, 'Check the __init__ functionality.')

    def test_name_setter(self):
        lap = get_laptop(name='Lenovo')
        with self.assertRaises(TypeError):
            lap.name = ''
        lap.name = 'Acer'
        self.assertEqual(lap.name, 'Acer', 'Check name setter.')

    def test_frequency_init(self):
        test_frequency = 1.2
        lap = get_laptop(frequency=test_frequency)
        self.assertEqual(lap.frequency, test_frequency, 'Check the __init__ functionality.')

    def test_frequency_set_negative(self):
        lap = get_laptop(frequency=1.2)
        with self.assertRaises(TypeError):
            lap.frequency = -2
        with self.assertRaises(TypeError):
            lap.frequency = 2
        lap.frequency = 2.1
        self.assertEqual(lap.frequency, 2.1, 'Check frequency setter.')

    def test_core_number_init(self):
        test_core_number = 1.2
        lap = get_laptop(frequency=test_core_number)
        self.assertEqual(lap.frequency, test_core_number, 'Check the __init__ functionality.')

    def test_core_number_setter(self):
        lap = get_laptop(core_number=4)
        with self.assertRaises(TypeError):
            lap.core_number = -2
        with self.assertRaises(TypeError):
            lap.core_number = 2.2
        lap.core_number = 2
        self.assertEqual(lap.core_number, 2, 'Check core_number setter.')

    def test_ram_init(self):
        test_ram = 8
        lap = get_laptop(ram=test_ram)
        self.assertEqual(lap.ram, test_ram, 'Check the __init__ functionality.')

    def test_ram_setter(self):
        lap = get_laptop(ram=4)
        with self.assertRaises(TypeError):
            lap.ram = -2
        with self.assertRaises(TypeError):
            lap.ram = 2.2
        lap.ram = 2
        self.assertEqual(lap.ram, 2, 'Check ram setter.')

    def test_hard_disk_init(self):
        test_hard_disk = 512
        lap = get_laptop(hard_disk=test_hard_disk)
        self.assertEqual(lap.hard_disk, test_hard_disk, 'Check the __init__ functionality.')

    def test_hard_disk_setter(self):
        lap = get_laptop(hard_disk=512)
        with self.assertRaises(TypeError):
            lap.hard_disk = -256
        with self.assertRaises(TypeError):
            lap.hard_disk = 'dfdf'
        lap.hard_disk = 1000
        self.assertEqual(lap.hard_disk, 1000, 'Check hard_disk setter.')

    def test_switch_on_off(self):
        lap = get_laptop()
        self.assertFalse(lap.switched_on, 'Check if the laptop is switched off after init.')
        lap.turn_on()
        self.assertTrue(lap.switched_on, 'Check if the laptop has been turned on.')
        lap.turn_on()
        self.assertTrue(lap.switched_on, 'Check if the laptop stay turned on.')
        lap.turn_off()
        self.assertFalse(lap.switched_on, 'Check if the laptop has been turned off.')


if __name__ == '__main__':
    unittest.main()
