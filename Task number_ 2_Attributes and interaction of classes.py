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

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_lecture(self, student, course, grade):
        if course in self.courses_attached and course in student.courses_in_progress:
            lecturer_name = f"{self.name} {self.surname}"
            if course in self.grades:
                self.grades[course].append({student: grade})
            else:
                self.grades[course] = [{student: grade}]
        else:
            return 'Ошибка'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_homework(self, student, course, grade):
        if course in self.courses_attached and course in student.courses_in_progress:
            student.grades[course] = student.grades.get(course, []) + [grade]
        else:
            return 'Ошибка'

# Пример использования классов
python_course_student = Student('Ruoy', 'Eman', 'your_gender')
python_course_student.courses_in_progress += ['Python']

python_lecturer = Lecturer('John', 'Doe')
python_lecturer.courses_attached += ['Python']

math_course_student = Student('Alice', 'Smith', 'female_gender')
math_course_student.courses_in_progress += ['Math']

math_lecturer = Lecturer('Jane', 'Smith')
math_lecturer.courses_attached += ['Math']

python_lecturer.rate_lecture(python_course_student, 'Python', 9)
math_lecturer.rate_lecture(math_course_student, 'Math', 8)

print(python_lecturer.grades)
print(math_lecturer.grades)