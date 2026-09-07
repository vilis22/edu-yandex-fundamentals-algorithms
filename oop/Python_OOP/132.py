import itertools


class Socks:
    _cycle = itertools.cycle(("левый", "правый"))

    def __init__(self):
        self.sock = next(self._cycle)


sock = Socks()
print(sock.sock)
sock = Socks()
print(sock.sock)
sock = Socks()
print(sock.sock)
