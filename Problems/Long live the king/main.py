row = int(input())
column = int(input())

if row in [1, 8] and column in [1, 8]:
    print(3)
elif row in [1, 8] or column in [1, 8]:
    print(5)
else:
    print(8)
