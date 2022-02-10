from exam_prepare_august_2020.exam_prepare_tird.hardware.heavy_hardware import HeavyHardware
from exam_prepare_august_2020.exam_prepare_tird.hardware.power_hardware import PowerHardware
from exam_prepare_august_2020.exam_prepare_tird.software.express_software import ExpressSoftware
from exam_prepare_august_2020.exam_prepare_tird.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        name = PowerHardware(name, capacity, memory)
        System._hardware.append(name)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        name = HeavyHardware(name, capacity, memory)
        System._hardware.append(name)

    @staticmethod
    def register_express_software(hardware_name, name, capacity, memory):
        for hardwares in System._hardware:
            if hardwares.name == hardware_name:
                names_of_software = ExpressSoftware(name, capacity, memory)
                hardwares.install(names_of_software)
                System._software.append(names_of_software)
                return
        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name, name, capacity, memory):
        for hardwares in System._hardware:
            if hardwares.name == hardware_name:
                names_of_software = LightSoftware(name, capacity, memory)
                hardwares.install(names_of_software)
                System._software.append(names_of_software)
                return
        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        is_exist_hard = False
        is_exist_soft = False
        s = ''
        h = ''
        for name in System._hardware:
            if name.name == hardware_name:
                h = name
                is_exist_hard = True
                break
        for name in System._software:
            if name.name == software_name:
                s = name
                is_exist_soft = True
                break
        if is_exist_soft and is_exist_hard:
            h.uninstall(s)
            return
        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_memory_hard = 0
        total_capacity_hard = 0
        total_memory_soft = 0
        total_capacity_soft = 0

        for hard in System._hardware:
            total_capacity_hard += hard.capacity
            total_memory_hard += hard.memory
        for soft in System._software:
            total_capacity_soft += soft.capacity_consumption
            total_memory_soft += soft.memory_consumption

        result = f"System Analysis\nHardware Components: {len(System._hardware)}\nSoftware Components: \
{len(System._software)}\nTotal Operational Memory: {total_memory_soft} / {total_memory_hard}\nTotal Capacity \
Taken: {total_capacity_soft} / {total_capacity_hard}"

        return result

    @staticmethod
    def system_split():
        results = []
        for hardwares in System._hardware:
            result = 'Hardware Component - '
            result += f'{hardwares.name}\n'
            result += f'Express Software Components: {len([s for s in hardwares.software_components if s.software_type == "Express"])}\n'
            result += f'Light Software Components: {len([s for s in hardwares.software_components if s.software_type == "Light"])}\n'
            result += f'Memory Usage: {sum([s.memory_consumption for s in hardwares.software_components])} / {hardwares.memory}\n'
            result += f'Capacity Usage: {sum([s.capacity_consumption for s in hardwares.software_components])} / {hardwares.capacity}\n'
            result += f'Type: {hardwares.hardware_type}\n'
            result += f'Software Components: {", ".join([s.name for s in hardwares.software_components])}'
            results.append(result)

        return '\n'.join(results)
