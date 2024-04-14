# Перегрузите магический метод __str__ у всех классов.

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_homework(self, student, course, grade):
        if course in self.courses_attached and course in student.courses_in_progress:
            student.grades[course] = student.grades.get(course, []) + [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return super().__str__()

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

# Пример использования классов
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_lecturer = Lecturer('Some', 'Buddy')
some_reviewer = Reviewer('Some', 'Buddy')

print(some_reviewer)
print(some_lecturer)
print(some_student)


# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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

    def __lt__(self, other):
        return self.grades_average() < other.grades_average()

    def grades_average(self):
        if self.grades:
            return sum([list(lecture.values())[0] for value in self.grades.values() for lecture in value]) / sum(len(value) for value in self.grades.values())
        else:
            return 0

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_homework(self, student, course, grade):
        if course in self.courses_attached and course in student.courses_in_progress:
            student.grades[course] = student.grades.get(course, []) + [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return super().__str__()

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

    def __lt__(self, other):
        return self.grades_average() < other.grades_average()

    def grades_average(self):
        return sum([grade for values in self.grades.values() for grade in values]) / sum(len(values) for values in self.grades.values())

# Пример использования
some_student1 = Student('Ruoy', 'Eman', 'your_gender')
some_student2 = Student('John', 'Doe', 'your_gender')
some_lecturer1 = Lecturer('Some', 'Buddy')
some_lecturer2 = Lecturer('Alice', 'Johnson')

print(some_lecturer1 < some_lecturer2)  # Сравнение лекторов
print(some_student1 < some_student2)    # Сравнение студентов