# 99 90 15 28 38 44 50 81 79 60 99 90 15 28 38 44 50 81 79 60
import sys

marks = []
above_average = []
sum1 = 0
average = 0.0
for mark in range(0, 10):
    mark = int(input("Please insert a mark: "))
    marks.append(mark)
    sum1 += mark
    average = sum1 / len(marks)
for m in marks:
    if m > average:
        above_average.append(m)
print(average)
print(marks)
print(above_average)
