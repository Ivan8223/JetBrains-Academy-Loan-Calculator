money = int(input())

if money >= 6769:
    amount = money // 6769
    print(f"{amount} sheep")
elif money >= 3848:
    amount = money // 3848
    print(f"{amount} {'cow' if amount == 1 else 'cows'}")
elif money >= 1296:
    amount = money // 1296
    print(f"{amount} {'pig' if amount == 1 else 'pigs'}")
elif money >= 678:
    amount = money // 678
    print(f"{amount} {'goat' if amount == 1 else 'goats'}")
elif money >= 23:
    amount = money // 23
    print(f"{amount} {'chicken' if amount == 1 else 'chickens'}")
else:
    print("None")
