from math import floor

from exam_prepare_august_2020.exam_prepare_tird.hardware.hardware import Hardware


class HeavyHardware(Hardware):

    def __init__(self, name, capacity, memory):
        super().__init__(name, 'Heavy', (capacity * 2), floor(memory * 0.75))

