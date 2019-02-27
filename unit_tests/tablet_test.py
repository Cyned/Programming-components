import unittest

from reflection import Tablet


def get_tablet(os_name='Android', diagonal=15.3, battery=10000,
               name='Lenovo', frequency=1.2, core_number=2, ram=4, hard_disk=64):
    return Tablet(
        os_name=os_name, diagonal=diagonal, battery=battery, name=name,
        frequency=frequency, core_number=core_number, ram=ram, hard_disk=hard_disk,
    )


class TestTablet(unittest.TestCase):

    def test_os_name_init(self):
        test_os_name = 'Android'
        tab = get_tablet(os_name=test_os_name)
        self.assertEqual(tab.os_name, test_os_name, 'Check the __init__ functionality.')

    def test_os_name_setter(self):
        tab = get_tablet(os_name='Android')
        with self.assertRaises(TypeError):
            tab.name = ''
        tab.os_name = 'IOS'
        self.assertEqual(tab.os_name, 'IOS', 'Check os_name setter.')

    def test_diagonal_init(self):
        test_diagonal = 15.0
        tab = get_tablet(diagonal=test_diagonal)
        self.assertEqual(tab.diagonal, test_diagonal, 'Check the __init__ functionality.')

    def test_diagonal_setter(self):
        tab = get_tablet(diagonal=15.0)
        with self.assertRaises(TypeError):
            tab.diagonal = -12.5
        with self.assertRaises(TypeError):
            tab.diagonal = 20
        tab.diagonal = 12.5
        self.assertEqual(tab.diagonal, 12.5, 'Check diagonal setter.')

    def test_battery_init(self):
        test_battery = 10000
        tab = get_tablet(battery=test_battery)
        self.assertEqual(tab.battery, test_battery, 'Check the __init__ functionality.')

    def test_battery_setter(self):
        tab = get_tablet(battery=10000)
        with self.assertRaises(TypeError):
            tab.battery = -5000
        with self.assertRaises(TypeError):
            tab.battery = 1235.3
        tab.battery = 8000
        self.assertEqual(tab.battery, 8000, 'Check battery setter.')


if __name__ == '__main__':
    unittest.main()
