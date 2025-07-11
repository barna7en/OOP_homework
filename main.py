from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return round(mean(all_grades), 1) if all_grades else None

    # переопределяем магические методы для студентов
    def __str__(self):
        avg_grade = self.average_grade()
        finished_courses_str = ', '.join(self.finished_courses)
        current_courses_str = ', '.join(self.courses_in_progress)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {current_courses_str}\nЗавершенные курсы: {finished_courses_str}'

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = [grade for grades_list in self.grades.values() for grade in grades_list]
        return round(mean(all_grades), 1) if all_grades else None

    # переопределяем магические методы для Лекторов
    def __str__(self):
        avg_grade = self.average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}'

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# Примеры использования
# Здесь мы определим студента, лектора и ревьювера
if __name__ == "__main__":
    best_student = Student('Руслан', 'Петухов', 'Мужской')
    some_lecturer = Lecturer('Сергей', 'Семёнович')
    some_reviewer = Reviewer('Александр', 'Александрович')
# Наш "лучший" (определим его в начале) студент закончил курс введение в программирование
    best_student.finished_courses.append('Введение в программирование')
# А так же курсы в процессе изучения "Python и Git"
    best_student.courses_in_progress.extend(['Python', 'Git'])
# Лектор ведет эти курсы
    some_lecturer.courses_attached.extend(['Python', 'Git'])
# Ревьювер проверяющий задания по этим курсам
    some_reviewer.courses_attached.extend(['Python', 'Git'])

    # Студенческие оценки за ДЗ
    some_reviewer.rate_hw(best_student, 'Python', 9)
    some_reviewer.rate_hw(best_student, 'Python', 8)
    some_reviewer.rate_hw(best_student, 'Git', 10)

    # Оценивание лектора
    best_student.rate_lecture(some_lecturer, 'Python', 9)
    best_student.rate_lecture(some_lecturer, 'Git', 8)

    # Добавим второго студента
    another_student = Student('Антон', 'Ковалёв', 'Мужской')

    # Второй студент изучает те же курсы
    another_student.courses_in_progress.extend(['Python', 'Git'])

    # Его оценки за проделанные работы
    some_reviewer.rate_hw(another_student, 'Python', 7)
    some_reviewer.rate_hw(another_student, 'Python', 6)
    some_reviewer.rate_hw(another_student, 'Git', 8)

    # Сравнение студентов и лекторов
    print("\nСтудент1:")
    print(best_student)
    print("\nСтудент2:")
    print(another_student)

    print("\nПреподаватель:")
    print(some_lecturer)

    print("\nЭксперт:")
    print(some_reviewer)

    print(f'\nЛучший студент лучше другого студента? {"Да" if best_student > another_student else "Нет"}')

    second_lecturer = Lecturer('Павел', 'Дмитриевич')
    second_lecturer.courses_attached.append('Python')
    best_student.rate_lecture(second_lecturer, 'Python', 10)

    print(f'\nПервый лектор хуже второго? {"Да" if some_lecturer < second_lecturer else "Нет"}')