scores = input().split()
# put your python code here

points = 0
lives = 3

for i in scores:
    if i == 'C':
        points += 1
        continue
    lives -= 1
    if lives == 0:
        print(f"Game over\n{points}")
        break
else:
    print(f"You won\n{points}")
