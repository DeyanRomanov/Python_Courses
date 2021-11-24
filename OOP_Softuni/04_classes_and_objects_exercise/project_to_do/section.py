from classes_and_objects_exercise.project_guild import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for t in self.tasks:
            if t.name == new_task.name:
                return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: Task):
        for t in self.tasks:
            if t.name == task_name:
                t.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_task_counter = 0

        for t in self.tasks:
            if t.completed:
                removed_task_counter += 1
                self.tasks.remove(t)

        return f"Cleared {removed_task_counter} tasks."

    def view_section(self):
        result = f"Section {self.name}:"

        for res in self.tasks:
            result += '\n'
            result += res.details()

        return result
