from car.muscle_car import MuscleCar
from car.sports_car import SportsCar
from driver import Driver
from race import Race


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in ["MuscleCar", "SportsCar"]:
            for cars in self.cars:
                if cars.model == model:
                    raise Exception(f"Car {model} is already created!")
            new_car = ''
            if car_type == 'MuscleCar':
                new_car = MuscleCar(model, speed_limit)
            elif car_type == 'SportsCar':
                new_car = SportsCar(model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for drivers in self.drivers:
            if drivers.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for races in self.races:
            if races.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver_for_race = ''
        is_driver_in = False
        for drivers in self.drivers:
            if drivers.name == driver_name:
                driver_for_race = drivers
                is_driver_in = True
                break
        if not is_driver_in:
            raise Exception(f"Driver {driver_name} could not be found!")
        cars_of_that_type = [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken]
        if not cars_of_that_type:
            raise Exception(f"Car {car_type} could not be found!")
        car_for_race = cars_of_that_type[-1]
        if driver_for_race.car is not None:
            result = f"Driver {driver_name} changed his car from {driver_for_race.car.model} to {car_for_race.model}."
            driver_for_race.car.is_taken = False
            car_for_race.is_taken = True
            driver_for_race.car = car_for_race
            return result
        car_for_race.is_taken = True
        driver_for_race.car = car_for_race
        return f"Driver {driver_name} chose the car {car_for_race.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver_for_race = ''
        pist_for_race = ''
        is_race = False
        for races in self.races:
            if races.name == race_name:
                pist_for_race = races
                is_race = True
                break
        if not is_race:
            raise Exception(f"Race {race_name} could not be found!")
        is_driver = False
        for drivers in self.drivers:
            if drivers.name == driver_name:
                is_driver = True
                driver_for_race = drivers
                break
        if not is_driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver_for_race.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver_for_race in pist_for_race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        pist_for_race.drivers.append(driver_for_race)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        is_exist = False
        race_for_now = ''
        for race in self.races:
            if race.name == race_name:
                is_exist = True
                race_for_now = race
                break
        if not is_exist:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race_for_now.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = {}
        for racers in race_for_now.drivers:
            winners[racers.car.speed_limit] = racers
        current_row = 0
        result = ''
        for k, v in sorted(winners.items(), key=lambda x: x[0], reverse=True):
            current_row += 1
            v.number_of_wins += 1
            result += f"Driver {v.name} wins the {race_name} race with a speed of {v.car.speed_limit}.\n"
            if current_row == 3:
                break

        return result.strip()
