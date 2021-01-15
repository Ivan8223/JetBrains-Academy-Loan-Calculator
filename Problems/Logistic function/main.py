from math import exp

x = int(input())

print(f"{round((1 / (exp(-x) + 1)), 2)}")
