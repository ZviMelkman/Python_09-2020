
class Summer:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self, num1, num2):
        return num1 + num2

    def print_total(self):
        print(f'{self.add()}')

# s = Summer()
# t = Summer()
#
# s.add(10, 20)
# t.add(50)
# s.add(30)
#
# # should print 60
# s.print_total()

# should print 50
t.print_total()