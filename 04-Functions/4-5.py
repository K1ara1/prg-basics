def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points > 13:
        grade = 'Good'
    elif points > 9:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'
    return grade

point = int(input('Enter points: '))
final_grade = pts_to_grade(point)
print(f'You scored {point} points on the test. Your final grade is {final_grade}')