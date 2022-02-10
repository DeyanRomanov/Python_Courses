from __exam_prepare_15_august_2021.project.table.table import Table


class InsideTable(Table):

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)
        
    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 1 or value > 50:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        self.__capacity = value
