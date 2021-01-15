student_score = float(input())
max_score = float(input())

percentages = student_score / max_score * 100

if percentages >= 90:
    print('A')
elif percentages >= 80:
    print('B')
elif percentages >= 70:
    print('C')
elif percentages >= 60:
    print('D')
else:
    print('F')
