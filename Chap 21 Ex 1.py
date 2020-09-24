
class Summer:

    num1 = 0
    num2 = 0

    def add(self):
        return self.num1 + self.num2

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
