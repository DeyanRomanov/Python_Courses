from project_hero.hero import Hero


class Wizard(Hero):

    def __init__(self, username: str, level: int):
        Hero.__init__(self, username, level)
