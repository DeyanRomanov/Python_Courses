from project_hero.elf import Elf


class MuseElf(Elf):
    def __init__(self, username: str, level: int):
        Elf.__init__(self, username, level)
