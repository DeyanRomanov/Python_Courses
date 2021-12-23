from exam_prepare_second.project.baked_food.cake import Cake
from exam_prepare_second.project.baked_food.bread import Bread
from exam_prepare_second.project.drink.tea import Tea
from exam_prepare_second.project.drink.water import Water
from exam_prepare_second.project.table.inside_table import InsideTable
from exam_prepare_second.project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        for foods in self.food_menu:
            if foods.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == 'Bread':
            food = Bread(name, price)
        else:
            food = Cake(name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        for drinks in self.drinks_menu:
            if drinks.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")
            if drink_type == 'Tea':
                drink = Tea(name, portion, brand)
            else:
                drink = Water(name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for tables in self.tables_repository:
            if tables.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == 'InsideTable':
            table = InsideTable(table_number, capacity)
        else:
            table = OutsideTable(table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for tables in self.tables_repository:
            if not tables.is_reserved and tables.capacity >= number_of_people:
                tables.reserve(number_of_people)
                return f"Table {tables.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, some_order):
        is_real_table = False
        for table in self.tables_repository:
            if table.table_number == table_number:
                is_real_table = True
                break
        if not is_real_table:
            return f"Could not find table {table_number}"
        ordered = []
        not_ordered = []
        args = some_order.split(', ')
        for food in args:
            for foods in self.food_menu:
                if food == foods.name:
                    ordered.append(foods)
                else:
                    not_ordered.append(food)
        result = f"Table {table_number} ordered:\n"
        for order in ordered:
            result += str(order) + '\n'
        result += f"{self.name} does not have in the menu:\n"
        for not_order in not_ordered:
            result += f'{not_order}\n'

        return result.strip()

    def order_drink(self, table_number: int, some_order):
        is_real_table = False
        for table in self.tables_repository:
            if table.table_number == table_number:
                is_real_table = True
                break
        if not is_real_table:
            return f"Could not find table {table_number}"
        ordered = []
        not_ordered = []
        args = some_order.split(', ')
        for drink in args:
            for drinks in self.food_menu:
                if drink == drinks.name:
                    ordered.append(drinks)
                else:
                    not_ordered.append(drink)
        result = f"Table {table_number} ordered:\n"
        for order in ordered:
            result += str(order) + '\n'
        result += f"{self.name} does not have in the menu:\n"
        for not_order in not_ordered:
            result += f'{not_order}\n'

        return result.strip()

    def leave_table(self, table_number: int):
        for tables in self.tables_repository:
            if tables.table_number == table_number:
                self.total_income += tables.get_bill()
                tables.clear()
                result = f"Table: {table_number}\nBill: {tables.get_bill()}"
                return result

    def get_free_tables_info(self):
        result = ''
        for tables in self.tables_repository:
            if not tables.is_reserved:
                result += tables.free_table_info() + '\n'

        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
