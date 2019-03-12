import unittest
from unittest.mock import patch

from mocki.controller import Controller


def get_controller(name='Lenovo', frequency=1.2, core_number=2, ram=4, hard_disk=64):
    return Controller(
        name=name, frequency=frequency, core_number=core_number, ram=ram, hard_disk=hard_disk,
    )


class TestLaptop(unittest.TestCase):
    @patch('Controller.get_name', return_value='Lenovo')
    def test(self):
        controller = get_controller()
        self.assertTrue(controller.get_name(), 'Lenovo')


if __name__ == '__main__':
    unittest.main()
