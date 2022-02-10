from math import floor

from exam_prepare_august_2020.exam_prepare_tird.hardware.hardware import Hardware


class PowerHardware(Hardware):

    def __init__(self, name, capacity, memory):
        super().__init__(name, 'Power', floor(capacity * 0.25), floor(memory * 1.75))

