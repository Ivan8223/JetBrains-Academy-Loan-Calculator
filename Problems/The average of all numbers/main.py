# put your python code here
a = int(input())
b = int(input())
mod3_list = []

for i in range(a, b + 1):
    if i % 3 == 0:
        mod3_list.append(i)

print(sum(mod3_list) / len(mod3_list))
