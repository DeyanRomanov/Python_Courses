from exam_prepare_august_2020.exam_prepare_tird.software.software import Software


class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        free_memory = (self.memory - sum([s.memory_consumption for s in self.software_components]))
        if software.memory_consumption <= free_memory:
            self.software_components.append(software)
            return
        raise Exception('Software cannot be installed')

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
            return
