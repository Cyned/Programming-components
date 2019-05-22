from lab6.patterns import Laptop


def get_output() -> dict:
    """ Returns information about the Laptop """
    output = dict()

    # Singleton
    output['Singleton'] = []
    laptop1 = Laptop('Lenovo')
    output['Singleton'].append(str(laptop1))

    laptop2 = Laptop('Acer')
    output['Singleton'].append(str(laptop2))

    output['Singleton'].append(str(laptop1 == laptop2))

    # Iterable
    output['Iterator'] = []
    for port in laptop1:
        output['Iterator'].append(str(port))

    return output
