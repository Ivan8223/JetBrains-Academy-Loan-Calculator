income = int(input())

if income >= 132407:
    percent = 28
elif income >= 42708:
    percent = 25
elif income >= 15528:
    percent = 15
else:
    percent = 0

print(f"The tax for {income} is {percent}%. "
      f"That is {(percent * income / 100):.0f} dollars!")
