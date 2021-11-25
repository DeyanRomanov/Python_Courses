from project_person.person import Person
from project_person.employee import Employee


class Teacher(Person, Employee):

    def teach(self):
        return 'teaching...'
