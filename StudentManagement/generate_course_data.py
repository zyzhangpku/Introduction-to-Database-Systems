import random
main_info = ['Elements', 'Fighting', 'Mathematics', 'Physics', 'History', 'English', 'Chinese', 'Software', 'Economics',
             'Biology', 'Finance']
pre = ['Introduction of', 'Principles of', 'Basics of', 'Advanced', 'Public', '', 'Intermediate']
honored = ['(Honor Track)', '']
sub1 = ['Engineering', 'Experiments', 'Practising', 'Modeling', '']
materials = [pre, main_info, sub1, honored]


def generate_course_name():
    name = ''
    for ele in materials:
        c = random.choice(ele)
        name += c
        if c:
            name += ' '
    return name.rstrip()


def generate_all_courses(n=1000):
    return set(generate_course_name() for _ in range(n))
