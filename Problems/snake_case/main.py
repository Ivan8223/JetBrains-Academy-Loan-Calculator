word = input()
res = word[0].lower()

for i in word[1:]:
    if i.isupper():
        res += '_' + i.lower()
    else:
        res += i

print(res)
