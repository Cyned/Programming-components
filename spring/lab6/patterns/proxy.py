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
