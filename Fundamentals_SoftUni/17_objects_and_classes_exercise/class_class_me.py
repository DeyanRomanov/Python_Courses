class Class:

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []
        self.__students_count = 22

    def add_student(self, name, grade):
        if len(self.students) < self.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.students)

    def __repr__(self):
        students_str = ', '.join(self.students)
        return f'The students in {self.name}: {students_str}. Average grade: {round(Class.get_average_grade(self), 2)}'
