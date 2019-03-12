import unittest
from unittest.mock import patch

from mocki.controller import Controller
from mocki.service import get_service


def get_controller():
    return Controller(name='Lenovo')


class TestLaptop(unittest.TestCase):
    @patch('mocki.service.input_str', return_value='test')
    @patch('mocki.service.input_number', return_value='1')
    def test_setters(self, input_number, input_str):
        controller = get_controller()
        new_name = input_str('Input new name')
        controller.set_name(new_name=new_name)
        self.assertEqual(controller.get_name(), 'test')

        hard_disk = input_number('Input new hard disk')
        controller.set_hard_disk(new_hard_disk=hard_disk)
        self.assertEqual(controller.get_hard_disk(), 1)

        new_ram = input_number('Input new ram')
        controller.set_ram(new_ram=new_ram)
        self.assertEqual(controller.get_ram(), 1)

        new_frequency = input_number('Input new frequency')
        controller.set_frequency(new_frequency=new_frequency)
        self.assertEqual(controller.get_ram(), 1.0)

    @patch('mocki.service.input_str', return_value='test')
    @patch('mocki.service.input_number', return_value='1')
    def test_get_service(self, input_number, input_str):
        controller = get_service()
        controller.set_name('Acer')
        self.assertEqual(controller.get_name(), 'Acer')

        input_str.assert_called()
        input_number.assert_called()


if __name__ == '__main__':
    unittest.main()
