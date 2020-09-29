
class Summer:

    def __init__(self, *numbers):
        self.numbers = numbers

    def add(self, *numbers):
        _sum = 0
        for i in self.numbers:
            _sum += self.numbers[i]
        return _sum

    def print_total(self):
        print(f'{self.add()}')


s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
s.print_total()

# should print 50
t.print_total()
