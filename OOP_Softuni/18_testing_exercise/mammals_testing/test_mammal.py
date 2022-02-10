from exam_prepare_august_2021.project import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Lucky', 'dog', 'woof-woof')

    def test_is_correct_implement(self):
        self.assertEqual('Lucky', self.mammal.name)
        self.assertEqual('dog', self.mammal.type)
        self.assertEqual('woof-woof', self.mammal.sound)

    def test_what_sound_make(self):
        self.assertEqual('Lucky makes woof-woof', self.mammal.make_sound())

    def test_what_kingdom_is(self):
        kingdom = self.mammal._Mammal__kingdom
        self.assertEqual("animals", kingdom)

    def test_get_kingdom(self):
        kingdom = self.mammal.get_kingdom()
        self.assertEqual("animals", kingdom)

    def test_what_info_returns(self):
        info = self.mammal.info()
        self.assertEqual('Lucky is of type dog', info)


if __name__ == "__main__":
    main()
