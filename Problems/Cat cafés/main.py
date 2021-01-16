input_string = ''
cafes = {}

while True:
    input_string = input()
    if input_string == 'MEOW':
        break
    else:
        cafe = input_string.split()
        cafes[cafe[0]] = int(cafe[1])
print(max(cafes, key=cafes.get))
