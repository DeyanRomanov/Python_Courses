from project_zoo import tiger
from project_zoo.worker import Worker
from project_zoo.animal import Animal


class Zoo:

    def __init__(self, name, budget, animal_capacity, worker_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals) and self.__budget >= price:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and not self.__budget >= price:
            return f"Not enough budget"
        return f"Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for workers in self.workers:
            if workers.name == worker_name:
                self.workers.remove(workers)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_sum_for_salary = 0
        for workers in self.workers:
            total_sum_for_salary += workers.salary
        if total_sum_for_salary > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_sum_for_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_sum_for_animals = 0
        for animals in self.animals:
            total_sum_for_animals += animals.money_for_care
        if total_sum_for_animals > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_sum_for_animals
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions_message = []
        tigers_message = []
        cheetahs_message = []
        message = f'You have {len(self.animals)} animals'
        for animal in self.animals:
            if type(animal).__name__ == 'Lion':
                lions_message.append(animal.__repr__())
            elif type(animal).__name__ == 'Tiger':
                tigers_message.append(animal.__repr__())
            else:
                cheetahs_message.append(animal.__repr__())
        message += f'\n----- {len(lions_message)} Lions:\n'
        message += '\n'.join(lions_message)
        message += f'\n----- {len(tigers_message)} Tigers:\n'
        message += '\n'.join(tigers_message)
        message += f'\n----- {len(cheetahs_message)} Cheetahs:\n'
        message += '\n'.join(cheetahs_message)
        return message

    def workers_status(self):
        keepers_workers = []
        caretakers_workers = []
        vets_workers = []
        message = f'You have {len(self.workers)} workers'
        for workers in self.workers:
            if type(workers).__name__ == 'Keeper':
                keepers_workers.append(workers.__repr__())
            elif type(workers).__name__ == 'Caretaker':
                caretakers_workers.append(workers.__repr__())
            else:
                vets_workers.append(workers.__repr__())
        message += f'\n----- {len(keepers_workers)} Keepers:\n'
        message += '\n'.join(keepers_workers)
        message += f'\n----- {len(caretakers_workers)} Caretakers:\n'
        message += '\n'.join(caretakers_workers)
        message += f'\n----- {len(vets_workers)} Vets:\n'
        message += '\n'.join(vets_workers)
        return message
