class Student:

    def __init__(self, name, surname, gender, score):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.score = score


    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += grade
            else:
                lecturer.grades[course] = grade
        else:
            return 'Ошибка'

    def __str__(self):
        if self.name in best_student1.name:
            return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {"%.2f"% average_score1}\nКурс в процессе изучения:{" ".join(best_student1.courses_in_progress)}\nЗавершенные курсы:{" ".join(best_student1.finished_courses)}'
        else:
            return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {"%.2f" % average_score2}\nКурс в процессе изучения:{" ".join(best_student2.courses_in_progress)}\nЗавершенные курсы:{" ".join(best_student2.finished_courses)}'

    def __lt__(self, other):
        return self.score < other.score

    # Создаем функцию для подчета ср значения оценок по всем студентам
    def average_all(self):
        self.list_students = []
        self.name_course = []
        self.grades = []



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname, average):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average = average

    def __str__(self):
        if self.name in cool_lecturer1.name:
            return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {"%.2f"% average_value1}'
        else:
            return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {"%.2f"% average_value2}'

    def __lt__(self, other):
        return self.average < other.average
class Reviewer(Mentor):

    def rate_reviewer(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

best_student1 = Student('Ruoy', 'Eman', 'your_gender', "score")
best_student1.courses_in_progress += ['Python']
best_student1.finished_courses += ['Git']
best_student2 = Student('Ivan', 'Ivanov', 'your_gender', 'score')
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Python']


cool_mentor1 = Mentor('Some', 'Buddy')
cool_mentor1.courses_attached += ['Python']
cool_mentor2 = Mentor('Chikki', 'Pikki')
cool_mentor2.courses_attached += ['Git']


cool_mentor1.rate_hw(best_student1, 'Python', [9, 6, 3])
average_score1 = sum(best_student1.grades["Python"])/len(best_student1.grades["Python"])
cool_mentor2.rate_hw(best_student2, 'Git', [8, 6, 10])
average_score2 = sum(best_student2.grades["Git"])/len(best_student2.grades["Git"])
print(best_student1.grades)
print(best_student2.grades)


cool_reviewer1 = Reviewer('Petr', 'Petrov')
cool_reviewer1.rate_reviewer(best_student1, 'Python', [6, 10, 10])
cool_reviewer2 = Reviewer('Sasha', 'Horoshii')
cool_reviewer2.rate_reviewer(best_student2, 'Git', [7, 5, 4])
print(best_student1.grades)
print(best_student2.grades)


cool_lecturer1 = Lecturer('Olga', 'Tereshenko', 'average')
cool_lecturer1.courses_attached += ['Python']
best_student1.rate_lecturer(cool_lecturer1, 'Python', [5, 8, 10])
average_value1 = sum(cool_lecturer1.grades['Python'])/len(cool_lecturer1.grades['Python'])
cool_lecturer2 = Lecturer('Sveta', 'Simonova', 'average')
cool_lecturer2.courses_attached += ['Git']
best_student2.rate_lecturer(cool_lecturer2, 'Git', [4, 7, 10])
average_value2 = sum(cool_lecturer2.grades['Git'])/len(cool_lecturer2.grades['Git'])
print(cool_lecturer1.grades)
print(cool_lecturer2.grades)
print()


some_reviewer1 = Reviewer(cool_reviewer1.name, cool_reviewer1.surname)
some_reviewer2 = Reviewer(cool_reviewer2.name, cool_reviewer2.surname)
print(some_reviewer1)
print(some_reviewer2)
print()

some_lecturer1 = Lecturer(cool_lecturer1.name, cool_lecturer1.surname, 'average')
some_lecturer2 = Lecturer(cool_lecturer2.name, cool_lecturer2.surname, 'average')
print(some_lecturer1)
print()
print(some_lecturer2)
print()


some_student1 = Student(best_student1.name, best_student1.surname, 'your_gender', 'score')
some_student2 = Student(best_student2.name, best_student2.surname, 'your_gender', 'score')
print(some_student1)
print()
print(some_student2)
print()


comparison_lecturer1 = Lecturer(cool_lecturer1.name, cool_lecturer1.surname, average_value1)
comparison_lecturer2 = Lecturer(cool_lecturer2.name, cool_lecturer2.surname, average_value2)
print(comparison_lecturer1 < comparison_lecturer2)
print()


comparison_student1 = Student(best_student1.name, best_student1.surname, 'gender', average_score1)
comparison_student2 = Student(best_student2.name, best_student2.surname, 'gender', average_score2)
print(comparison_student1 < comparison_student2)
print()
# Находим среднее по всем студентам
all_students = Student('name', 'surname', 'your_gender', "score")
all_students.average_all()
all_students.list_students += [f'{best_student1.name} {best_student1.surname}', f'{best_student2.name} {best_student2.surname}']
all_students.name_course += ['Python', 'Git']
all_students.grades += [best_student1.grades["Python"], best_student2.grades["Git"]]
z = 0
for i in all_students.grades:
    for x in i:
        z += x
average = z/(len(best_student1.grades["Python"]) + len(best_student2.grades["Git"]))
print('Среднее значение все студентов: ', average)



