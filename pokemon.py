class Pokemon:
    def __init__(self, names, health):
        self.names = names
        self.health = health

    def pokemon_details(self):
        return f"{self.names} with health {self.health}"

