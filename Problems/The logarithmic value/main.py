from math import log

number = int(input())
base = int(input())

if base < 0 or base in [0, 1]:
    print(f"{log(number):.2f}")
else:
    print(f"{log(number, base):.2f}")
