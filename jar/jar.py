class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("incorrect capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return ("🍪" * self._size)

    def deposit(self, n):
        self._size += n
        if self.size > self.capacity:
            raise ValueError("Exceed Capacity")

    def withdraw(self, n):
        self._size -= n
        if self.size < 0:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(3)
jar.withdraw(1)
print(jar)