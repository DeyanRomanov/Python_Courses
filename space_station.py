from astronaut.astronaut_repository import AstronautRepository
from planet.planet_repository import PlanetRepository
from astronaut.biologist import Biologist
from astronaut.geodesist import Geodesist
from astronaut.meteorologist import Meteorologist
from planet.planet import Planet


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_mission = {'yes': 0,
                                   'no': 0
                                   }

    def add_astronaut(self, astronaut_type, astronaut_name):
        if self.astronaut_repository.find_by_name(astronaut_name):
            return f"{astronaut_name} is already added."
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")
        if astronaut_type == 'Biologist':
            astronaut_name = Biologist(astronaut_name)
        elif astronaut_type == 'Geodesist':
            astronaut_name = Geodesist(astronaut_name)
        elif astronaut_type == 'Meteorologist':
            astronaut_name = Meteorologist(astronaut_name)
        self.astronaut_repository.add(astronaut_name)
        return f"Successfully added {astronaut_type}: {astronaut_name.name}."

    def add_planet(self, name, items):
        for planets in self.planet_repository.planets:
            if planets.name == name:
                return f"{name} is already added."
        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        result = self.astronaut_repository.find_by_name(name)
        if result:
            self.astronaut_repository.remove(result)
            return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self, ):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name):
        self.successful_mission['no'] += 1
        sorted_all_astronauts = {}
        astronaut_for_mission = []
        is_planet_in_repository = False
        current = ''
        for planets in self.planet_repository.planets:
            if planets.name == planet_name:
                current = planets
                is_planet_in_repository = True
                break
        if not is_planet_in_repository:
            raise Exception("Invalid planet name!")
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                sorted_all_astronauts[astronaut.oxygen] = astronaut
        if len(sorted_all_astronauts) < 1:
            raise Exception("You need at least one astronaut to explore the planet!")
        for oxy, astro in sorted(sorted_all_astronauts.items(), reverse=True, key=lambda x: x[0]):
            if len(astronaut_for_mission) < 5:
                astronaut_for_mission.append(astro)
            else:
                break
        astronaut_for_mission_2 = []
        astronaut_for_mission_2 = astronaut_for_mission.copy()
        while self.planet_repository.planets.current_planet.items:
            if astronaut_for_mission[0].oxygen >= astronaut_for_mission[0].BREATH_UNIT:
                astronaut_for_mission[0].backpack.append(self.planet_repository.planets.current.items.pop())
                astronaut_for_mission[0].breathe()
                self.astronaut_repository.astronauts.astronaut_for_mission[0].oxygen = astronaut_for_mission[0].oxygen
            else:
                astronaut_for_mission.pop(0)

            if not astronaut_for_mission and len(self.planet_repository.planets.current_planet.items) > 0:
                return "Mission is not completed."

        astro = 0
        for oxy, astron in sorted_all_astronauts.items():
            for astronaut in astronaut_for_mission_2:
                if astron == astronaut and astronaut.oxygen != oxy:
                    astro += 1

        self.successful_mission['no'] -= 1
        self.successful_mission['yes'] += 1
        return f"Planet: {planet_name} was explored. {astro} astronauts participated in collecting items."

    def report(self):
        result = f"{self.successful_mission['yes']} successful missions!\n{self.successful_mission['no']} missions were not completed!\nAstronauts' info:"
        for astronaut in self.astronaut_repository.astronauts:
            if len(astronaut.backpack) == 0:
                astronaut.backpack = 'none'
            else:
                astronaut.backpack = ', '.join(astronaut.backpack)
            result += f"\nName: {astronaut.name}\nOxygen: {astronaut.oxygen}\nBackpack items: {astronaut.backpack}"

        return result
