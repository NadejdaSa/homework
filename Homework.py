def get_avg_grade(man):
    sum_grades, number_grades = 0, 0
    for course in man.grades:
        sum_grades += sum(man.grades[course])
        number_grades += len(man.grades[course])
    if number_grades == 0:
        average_grade = 0
    else:
        average_grade = sum_grades / number_grades
    return average_grade


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {get_avg_grade(self)}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}"""
    
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    
    def __lt__(self, student):
        return get_avg_grade(self) < get_avg_grade(student)
    
    def __le__(self, student):
        return get_avg_grade(self) <= get_avg_grade(student)
    
    def __eq__(self, student):
        return get_avg_grade(self) == get_avg_grade(student)
    
    def __ne__(self,student):
        return get_avg_grade(self) != get_avg_grade(student)
    
    def __ge__(self,student):
        return get_avg_grade(self) >= get_avg_grade(student)

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {get_avg_grade(self)}"""

    def __lt__(self, lecturer):
        return get_avg_grade(self) < get_avg_grade(lecturer)
    
    def __le__(self, lecturer):
        return get_avg_grade(self) <= get_avg_grade(lecturer)
    
    def __eq__(self, lecturer):
        return get_avg_grade(self) == get_avg_grade(lecturer)
    
    def __ne__(self, lecturer):
        return get_avg_grade(self) != get_avg_grade(lecturer)
    
    def __ge__(self, lecturer):
        return get_avg_grade(self) >= get_avg_grade(lecturer)

class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}"""

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 

def middle_grade_student(students_list, course):
    sum_grades, number_grades = 0, 0
    for student in students_list:
        if course in student.grades:
            sum_grades += sum(student.grades[course])
            number_grades += len(student.grades[course])
    if number_grades == 0:
        average_grade = 0
    else:
        average_grade = sum_grades / number_grades
    return average_grade

def middle_grade_lecturer(lecturers_list, course):
    sum_grades, number_grades = 0, 0
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            sum_grades += sum(lecturer.grades[course])
            number_grades += len(lecturer.grades[course])
    if number_grades == 0:
        average_grade = 0
    else:
        average_grade = sum_grades / number_grades
    return average_grade

lecturer_mandy = Lecturer('Mandy', 'Thompson')
lecturer_mandy.courses_attached += ['Reading Books', 'Searching in Deck']

lecturer_nathaniel = Lecturer('Nathaniel', 'Cho')
lecturer_nathaniel.courses_attached += ['Fighting']

reviewer_vincent = Reviewer('Vincent', 'Lee')
reviewer_vincent.courses_attached += ['Reading Books', 'Searching in Deck']

reviewer_zoey = Reviewer('Zoey', 'Samaras')
reviewer_zoey.courses_attached += ['Fighting']

student_amina = Student('Amina', 'Zidane', 'female')
student_amina.courses_in_progress += ['Reading Books', 'Fighting']
student_amina.finished_courses = ['Searching in Deck']

student_tommy = Student('Tommy', 'Maldoon', 'male')
student_tommy.courses_in_progress += ['Fighting', 'Searching in Deck']
student_tommy.finished_courses += ['Reading Books']

student_amina.rate_lecture(lecturer_mandy, 'Reading Books', 10)
student_amina.rate_lecture(lecturer_mandy, 'Reading Books', 8)
student_amina.rate_lecture(lecturer_nathaniel, 'Fighting', 9)
student_amina.rate_lecture(lecturer_nathaniel, 'Fighting', 4)

student_tommy.rate_lecture(lecturer_nathaniel, 'Fighting', 8)
student_tommy.rate_lecture(lecturer_nathaniel, 'Fighting', 7)
student_tommy.rate_lecture(lecturer_mandy, 'Searching in Deck', 8)
student_tommy.rate_lecture(lecturer_mandy, 'Searching in Deck', 10)

reviewer_vincent.rate_hw(student_amina, 'Reading Books', 7)
reviewer_vincent.rate_hw(student_amina, 'Reading Books', 9)
reviewer_vincent.rate_hw(student_tommy, 'Searching in Deck', 6)
reviewer_vincent.rate_hw(student_tommy, 'Searching in Deck', 5)

reviewer_zoey.rate_hw(student_amina, "Fighting", 2)
reviewer_zoey.rate_hw(student_amina, "Fighting", 5)
reviewer_zoey.rate_hw(student_tommy, "Fighting", 8)
reviewer_zoey.rate_hw(student_tommy, "Fighting", 7)

print(lecturer_mandy)

print(lecturer_nathaniel)

print(reviewer_vincent)

print(reviewer_zoey)

print(student_amina)

print(student_tommy)

print(lecturer_mandy < lecturer_nathaniel)
print(lecturer_mandy <= lecturer_nathaniel)
print(lecturer_mandy == lecturer_nathaniel)
print(lecturer_mandy != lecturer_nathaniel)
print(lecturer_mandy >= lecturer_nathaniel)

print(student_amina < student_tommy)
print(student_amina <= student_tommy)
print(student_amina == student_tommy)
print(student_amina != student_tommy)
print(student_amina >= student_tommy)

lecturers_list = [lecturer_mandy, lecturer_nathaniel]
students_list = [student_amina, student_tommy]

print(f'Средняя оценка за домашние задания по курсу "Reading Books": {middle_grade_student(students_list, "Reading Books")}')
print(f'Средняя оценка за домашние задания по курсу "Fighting": {middle_grade_student(students_list, "Fighting")}')
print(f'Средняя оценка за домашние задания по курсу "Searching in Deck": {middle_grade_student(students_list, "Searching in Deck")}')

print(f'Средняя оценка за лекции по курсу "Reading Books": {middle_grade_student(lecturers_list, "Reading Books")}')
print(f'Средняя оценка за лекции по курсу "Fighting": {middle_grade_student(lecturers_list, "Fighting")}')
print(f'Средняя оценка за лекции по курсу "Searching in Deck": {middle_grade_student(lecturers_list, "Searching in Deck")}')