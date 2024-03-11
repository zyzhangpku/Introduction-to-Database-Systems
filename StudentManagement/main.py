from datetime import datetime
from students import Student
import csv

filepath = r'.\data\students.csv'
print('Loading...')


def get_info(info):
    print('Please enter ' + info)
    m = input()
    if info == 'q':
        return False
    return m


def get_all_courses(csv_filename):
    with open(csv_filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        course_names = header[5:]
    return course_names


all_courses = get_all_courses(r'.\data\students.csv')


def get_student():
    name = get_info('name')
    if not name:
        return
    print('Please enter ID number')
    id_num = input()
    if id_num == 'q':
        return
    if not id_num.isdigit():
        print('The ID number is not valid.')
        return

    print('Please enter birthday, in the form like:2024-2-25')
    birthday = input()

    def is_valid_date(date_string):
        try:
            date_string = datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    if birthday == 'q':
        return
    if not is_valid_date(birthday):
        print('The birthday is not valid.')
        return
    college = get_info('college')
    if not college:
        return
    department = get_info('department')
    if not department:
        return
    print('Now you are adding the courses and grades. Enter the letter s to save this student\'s info.')
    d = {}
    while True:
        course = get_info('a course selected')
        if not course:
            return
        if course == 's':
            break
        if course not in all_courses:
            print('This class does not exist.')
            return
        grade = input('Please enter the grade\n')
        if grade == 'q':
            return
        if not grade.isdigit() or int(grade) < 0 or int(grade) > 100:
            print('The grade is not valid.')
            return
        grade = int(grade)
        d[course] = grade
    ans = Student(name, id_num, birthday, college, department, d)
    return ans


def add_student_csv(csv_filename, s: Student):
    with open(csv_filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # The first row is the header
        student_courses = s.courses
        student_row = [s.name, s.id_num, s.birthday, s.college, s.department] + [0] * (len(header) - 5)
    for course, grade in student_courses.items():
        if course in header:
            course_index = header.index(course)
            student_row[course_index] = grade
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student_row)


def add_student():
    print('--Now you are adding a student--')
    print('!!If you want to quit, please enter the letter q!!')
    s = get_student()
    add_student_csv(r'.\data\students.csv', s)
    print('You add a student. Here is the information of this student:')
    print(s)


def get_student_names(csv_filename):
    student_names = []
    with open(csv_filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row:  # Make sure the row is not empty
                student_names.append(row[0])  # Assume the first element is the student's name
    return student_names


def delete_student():
    all_students = get_student_names(r'.\data\students.csv')
    print('--Now you are deleting a student\'s information')
    print('!!If you want to quit, please enter the letter q!!')
    s = input('Please enter student\'s name\n')
    if s not in all_students:
        print('Cannot find this student')
        return
    if s == 'q':
        return
    delete_student_from_csv(filepath, s)
    print('Delete Successfully')


def delete_student_from_csv(csv_filename, student_name_to_delete):
    lines = []
    deleted = False
    with open(csv_filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != student_name_to_delete:
                lines.append(row)
            else:
                deleted = True
    if deleted:
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lines)
        return True
    else:
        return False


def update_student_info(csv_filename, student_name, updated_courses):
    updated_data = []
    student_found = False

    with open(csv_filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        updated_data.append(header)

        for row in reader:
            if row[0] == student_name:
                student_found = True
                for course, grade in updated_courses.items():
                    if course in header:
                        course_index = header.index(course)
                        row[course_index] = grade
            updated_data.append(row)

    if student_found:
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(updated_data)
        return True
    else:
        print('Student not found')
        return False


def update_student():
    print('--Now you are updating a student\'s info--')
    print('!!If you want to quit, please enter the letter q!!')
    print('!!If you want to skip one item, please enter the letter p!!')
    d = {}
    name = get_info('name')
    if not name:
        return
    print('Please enter ID number')
    id_num = input()
    if id_num == 'p':
        pass
    elif id_num == 'q':
        return
    elif not id_num.isdigit():
        print('The ID number is not valid.')
        return
    else:
        d['ID'] = int(id_num)
    print('Please enter birthday, in the form like:2024-2-25')
    birthday = input()

    def is_valid_date(date_string):
        try:
            date_string = datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    if birthday == 'p':
        pass
    elif birthday == 'q':
        return
    elif not is_valid_date(birthday):
        print('The birthday is not valid.')
        return
    else:
        d['Birthday'] = birthday

    college = get_info('college')
    if college == 'p':
        pass
    elif not college:
        return
    else:
        d['College'] = college
    department = get_info('department')
    if department == 'p':
        pass
    elif not department:
        return
    else:
        d['Department'] = department
    print('Now you are adding the courses and grades. Enter the letter s to save this student\'s info.')
    while True:
        course = get_info('a course selected')
        if course == 'p':
            break
        if not course:
            return
        if course == 's':
            break
        if course not in all_courses:
            print('This class does not exist.')
            return
        grade = input('Please enter the grade\n')
        if grade == 'q':
            return
        if not grade.isdigit() or int(grade) < 0 or int(grade) > 100:
            print('The grade is not valid.')
            return
        grade = int(grade)
        d[course] = grade
    ans = Student(name, id_num, birthday, college, department, d)
    print(ans.courses)
    update_student_csv(filepath, name, {
        'ID Number': id_num, 'Birthday': birthday, 'College': college,
        'Department': department
    }, d)
    return ans


def update_student_csv(csv_filename, student_name, updated_courses, d):
    updated_data = []
    student_found = False

    with open(csv_filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        updated_data.append(header)
        for row in reader:
            if row[0] == student_name:
                student_found = True
                for course, grade in list(updated_courses.items()) + list(d.items()):
                    if course in header and grade != 'p':
                        course_index = header.index(course)
                        row[course_index] = grade
            updated_data.append(row)

    if student_found:
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(updated_data)
            print('Update successfully')
        return True
    else:
        return False


def get_student_grades(csv_filename, ):
    print('--Now you are asking for a student\'s info--')
    student_grades = {}
    student_name = input('Please enter the name or ID\n')

    with open(csv_filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Read the header to get the courses names

        for row in reader:
            if row[1] == student_name:
                student_name = row[0]
            if row[0] == student_name:
                # Combine the courses (header) with the grades (row)
                student_grades = dict(zip(header[1:], row[1:]))
                break

    print(f"{student_name}'s information:")
    if student_grades:
        for course, grade in student_grades.items():
            if grade != '0':
                print(f"{course}: {grade}")
    else:
        print(f"No record found for {student_name}.")


while True:
    m = 'Enter a, d, u, i for adding, deleting, updating, inquire student\'s information'
    print(m)
    print('Enter Q to quit')
    s = input()
    try:
        if s == 'Q':
            print('Bye')
            break
        elif s == 'a':
            add_student()
        elif s == 'd':
            delete_student()
        elif s == 'u':
            update_student()
        elif s == 'i':
            get_student_grades(filepath)
    except:
        print('Error, please try again')
