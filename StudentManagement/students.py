class Student:
    def __init__(self, name, id_num, birthday, college, department, courses={}):
        self.name = name
        self.courses = courses
        self.id_num = id_num
        self.birthday = birthday
        self.college = college
        self.department = department

    def __str__(self):
        course_info = ''
        if not self.courses:
            course_info = '\tNo courses selected'
        else:
            for course, grade in self.courses.items():
                if grade > 0:
                    course_info += f'\t{course}: {grade}\n'
        return f'Name: {self.name}\nID Number: {self.id_num}\nBirthday: {self.birthday}\nCollege: {self.college}\n' \
               f'Department: {self.department}\nCourses Grades:\n{course_info} '
