phone_number = input()
numbers_str = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three',
               '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
               '8': 'eight', '9': 'nine', '10': 'ten'}

for i in phone_number:
    print(numbers_str[str(i)])