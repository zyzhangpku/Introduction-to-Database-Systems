import random
import csv
from students import Student
import generate_student_data
import generate_course_data
print('Initializing...')
all_students = list(set(generate_student_data.generate_all_students(n=10000)))
all_courses = list(set(generate_course_data.generate_all_courses(n=500)))
students = []
for i in range(len(all_students)):
    s = Student(all_students[i], 220000000 + i, generate_student_data.random_date(),
                random.choice(['yp', 'xk', 'dk', 'sms', 'gsm', 'jy', 'wy', 'fy', 'sky']),
                'No.' + str(random.randint(1, 10))
                )
    courses = random.choices(all_courses, k=random.randint(4, 8))
    d = {}
    for k in all_courses:
        if k in courses:
            d[k] = random.randint(60, 100)
        else:
            d[k] = 0
    s.courses = d
    students.append(s)
with open(r'.\data\students.csv', mode='w', newline='') as f:

    writer = csv.writer(f)
    writer.writerow(['Name', 'ID', 'Birthday', 'College', 'Department'] + all_courses)
    for student in students:
        info = [student.name, student.id_num, student.birthday, student.college, student.department]
        for course in all_courses:
            info.append(student.courses[course])
        writer.writerow(info)
    print('Done.')
