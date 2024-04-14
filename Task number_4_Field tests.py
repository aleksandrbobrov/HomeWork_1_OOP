class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_lecture(self, student, course, grade):
        if course in self.courses_attached and course in student.courses_in_progress:
            if course in self.grades:
                self.grades[course].append({student: grade})
            else:
                self.grades[course] = [{student: grade}]
        else:
            return 'Ошибка'

    def __str__(self):
        if self.grades:
            average_grade = sum([list(lecture.values())[0] for value in self.grades.values() for lecture in value]) / sum(len(value) for value in self.grades.values())
            return super().__str__() + f'\nСредняя оценка за лекции: {average_grade:.1f}'
        else:
            return super().__str__() + '\nСредняя оценка за лекции: N/A'

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['Введение в программирование']
        self.courses_in_progress = ['Python', 'Git']
        self.grades = {'Python': [9, 10, 8], 'Git': [10, 10, 9]}

    def __str__(self):
        average_grade = sum([grade for values in self.grades.values() for grade in values]) / sum(len(values) for values in self.grades.values())
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

# Создание экземпляров классов
student1 = Student('Ruoy', 'Eman', 'Male')
student2 = Student('John', 'Doe', 'Male')

lecturer1 = Lecturer('Alice', 'Johnson')
lecturer2 = Lecturer('Bob', 'Smith')

# Вызов всех созданных методов
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)

# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def average_grade_for_course(students, course_name):
    grades_sum = sum([student.grades.get(course_name, []) for student in students], [])
    return sum(grades_sum) / len(grades_sum) if len(grades_sum) > 0 else 0

# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def average_grades_for_lecturers(lecturers, course_name):
    grades_sum = sum([sum([list(lecture.values())[0] for lecture in lecturer.grades.get(course_name, [])]) for lecturer in lecturers])
    lectures_count = sum([len(lecturer.grades.get(course_name, [])) for lecturer in lecturers])
    return grades_sum / lectures_count if lectures_count > 0 else 0

# Пример вызова функций
students = [student1, student2]
lecturers = [lecturer1, lecturer2]

course_name = 'Python'
print(f'Средняя оценка за домашние задания по курсу {course_name}: {average_grade_for_course(students, course_name):.1f}')

print(f'Средняя оценка за лекции по курсу {course_name}: {average_grades_for_lecturers(lecturers, course_name):.1f}')