from __exam_prepare_15_august_2021.project.table.table import Table


class OutsideTable(Table):

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 51 or value > 101:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
        self.__capacity = value
