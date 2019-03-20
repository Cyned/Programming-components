import unittest
from unittest.mock import patch

from mocki.controller import Controller
from reflection.laptop import Laptop


def get_controller(name='Acer', frequency=1.2, core_number=2, ram=4, hard_disk=64):
    contr = Controller()
    contr.laptop = Laptop(
        name=name, frequency=frequency, core_number=core_number, ram=ram, hard_disk=hard_disk,
    )
    return contr


class TestLaptop(unittest.TestCase):

    @patch('mocki.service.input_str', return_value='Acer')
    @patch('mocki.service.input_int', return_value='1')
    @patch('mocki.service.input_float', return_value='1.2')
    def test_get_service(self, input_float, input_int, input_str):
        controller = get_controller()
        controller.create_laptop()
        self.assertEqual(controller.laptop.name, 'Acer')
        input_float.assert_called()
        input_str.assert_called()
        input_int.assert_called()

        # controller.update_cores()
        # self.assertEqual(controller.laptop.core_number, 1)
        #
        # input_int.assert_called()

    @patch('mocki.controller.input_str', return_value='Acer')
    @patch('mocki.controller.input_int', return_value='1')
    @patch('mocki.controller.input_float', return_value='1.2')
    def test_setters(self, input_float, input_int, input_str):
        controller = get_controller()
        controller.update_name()
        self.assertEqual(controller.laptop.name, 'Acer')

        controller.update_cores()
        self.assertEqual(controller.laptop.core_number, 1)

        controller.update_frequency()
        self.assertEqual(controller.laptop.frequency, 1.2)

        controller.update_ram()
        self.assertEqual(controller.laptop.ram, 1)

        controller.update_hard_disk()
        self.assertEqual(controller.laptop.hard_disk, 1)


if __name__ == '__main__':
    unittest.main()
