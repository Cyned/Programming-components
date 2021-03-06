import abc


class Invoker:
    """
    Ask the command to carry out the request.
    """

    def __init__(self):
        self._commands = []

    def store_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()


class Command(metaclass=abc.ABCMeta):
    """
    Declare an interface for executing an operation.
    """

    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    """
    Define a binding between a Receiver object and an action.
    Implement Execute by invoking the corresponding operation(s) on
    Receiver.
    """

    def execute(self):
        self._receiver.turn_on()


class Laptop(object):

    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f'{self.name} turning on...')


if __name__ == '__main__':
    laptop1 = Laptop('Acer')
    laptop2 = Laptop('Lenovo')
    concrete_command1 = ConcreteCommand(laptop1)
    concrete_command2 = ConcreteCommand(laptop2)
    invoker = Invoker()
    invoker.store_command(concrete_command1)
    invoker.store_command(concrete_command2)
    invoker.execute_commands()
