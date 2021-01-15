from math import radians
from math import tan

deg_angle = int(input())

print(f"{1 / tan(radians(deg_angle)):.10f}")
