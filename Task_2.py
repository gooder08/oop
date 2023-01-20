class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    # Студенты могут оценивать лекторов
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
class Reviewer(Mentor):
    # Эксперты оценивают студентов
    def rate_reviewer(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student1 = Student('Ruoy', 'Eman', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.finished_courses += ['Git']
best_student2 = Student('Ivan', 'Ivanov', 'your_gender')
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Python']


cool_mentor1 = Mentor('Some', 'Buddy')
cool_mentor1.courses_attached += ['Python']
cool_mentor2 = Mentor('Chikki', 'Pikki')
cool_mentor2.courses_attached += ['Git']

# Менторы оценивают студентов
cool_mentor1.rate_hw(best_student1, 'Python', 9)
cool_mentor2.rate_hw(best_student2, 'Git', 8)
print(best_student1.grades)
print(best_student2.grades)

# Эксперты оценивают студентов (добавляется к оценке менторов)
cool_reviewer1 = Reviewer('Petr', 'Petrov')
cool_reviewer1.rate_reviewer(best_student1, 'Python', 6)
cool_reviewer2 = Reviewer('Sasha', 'Horoshii')
cool_reviewer2.rate_reviewer(best_student2, 'Git', 7)
print(best_student1.grades)
print(best_student2.grades)

# Студенты оценивают лектора
cool_lecturer1 = Lecturer('Olga', 'Tereshenko')
cool_lecturer1.courses_attached = ['Python']
best_student1.rate_lecturer(cool_lecturer1, 'Python', 5)
cool_lecturer2 = Lecturer('Sveta', 'Simonova')
cool_lecturer2.courses_attached = ['Python']
best_student2.rate_lecturer(cool_lecturer2, 'Git', 4)
print(cool_lecturer1.grades)
print(cool_lecturer2.grades)