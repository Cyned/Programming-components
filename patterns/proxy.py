class Laptop:
    def __init__(self, name):
        self.name = name
        self.switched_on = False

    def turn_on(self):
        self.switched_on = True
        print(f"{self.name} turning on...")

    def turn_off(self):
        self.switched_on = False
        print(f"{self.name} turning off...")

    def get_user(self):
        """ Print user logged in """
        return 'denis'


class Proxy:
    def __init__(self, subject):
        self.subject = subject
        self.proxy_state = None


class ProxyLaptop(Proxy):
    def print(self):
        if self.proxy_state is None:
            self.subject.turn_on()
            self.proxy_state = 1
        print(f'Display {self.subject.name}`s user: {self.subject.get_user()}')


if __name__ == '__main__':
    proxy_laptop1 = ProxyLaptop(Laptop("Acer"))
    proxy_laptop2 = ProxyLaptop(Laptop("Lenovo"))

    proxy_laptop1.print()  # loading necessary
    proxy_laptop1.print()  # loading unnecessary
    proxy_laptop2.print()  # loading necessary
    proxy_laptop2.print()  # loading unnecessary
    proxy_laptop1.print()  # loading unnecessary
