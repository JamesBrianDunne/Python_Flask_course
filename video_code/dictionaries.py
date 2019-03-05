
my_set = {1, 3, 5}
my_dict = {'name': 'Jose', 'age': 90, 'grades': [13, 45, 66, 90]}
another_dict = {1: 15, 2: 75, 3: 150}

lottery_player =[
    {
        'name': 'Rolf',
        'numbers': (13, 45, 66, 23, 22)
    },
    {
        'name': 'John',
        'numbers': (14, 56, 80, 23, 22)
    }
]

universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
]

sum(lottery_player['numbers'])
#lottery_player['name'] = 'John'
#print(lottery_player['name'])

student = {'name': 'Jose', 'school': 'Computing', 'grades': (66, 77, 88)}

def average_grade(data):
    grades = data['grades']
    return sum(grades) / len(grades)


def average_grade_all_students(student_list):
    total = 0
    count = 0
    for s in student_list:
        total += sum(s['grades'])
        count += len(s['grades'])

    return total / count