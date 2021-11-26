from project_hero.wizard import Wizard


class DarkWizard(Wizard):

    def __init__(self, username: str, level: int):
        Wizard.__init__(self, username, level)
