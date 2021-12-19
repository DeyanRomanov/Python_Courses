from exam_prepare.project import Hero

from unittest import TestCase, main


class HeroTest(TestCase):
    def setUp(self):
        self.hero = Hero('Wizard', 10, 77.7, 15.2)

    def test_initialised_hero(self):
        self.assertEqual('Wizard', self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(77.7, self.hero.health)
        self.assertEqual(15.2, self.hero.damage)

    def test_raise_if_battle_with_himself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_value_error_if_enemy_health_less_than_zero(self):
        self.hero_2 = Hero('Viktor', 10, -77.7, 15.2)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.hero_2)
        self.assertEqual("You cannot fight Viktor. He needs to rest", str(ex.exception))

    def test_myself_health_raise_if_less_than_zero(self):
        self.hero_2 = Hero('Viktor', 10, -77.7, 15.2)
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.hero_2)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle_if_not_raise_error_and_finish_draw(self):
        self.hero = Hero('Wizard', 10, 10, 10)
        self.hero_2 = Hero('Viktor', 10, 10, 10)
        result = self.hero.battle(self.hero_2)
        self.assertEqual('Draw', result)

    def test_battle_if_my_hero_win(self):
        self.hero_2 = Hero('Viktor', 5, 9, 5)
        result = self.hero.battle(self.hero_2)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(57.7, self.hero.health)
        self.assertEqual(20.2, self.hero.damage)
        self.assertEqual('You win', result)

    def test_battle_if_my_hero_lost(self):
        self.hero_2 = Hero('Viktor', 10, 200, 10)
        result = self.hero.battle(self.hero_2)
        self.assertEqual(11, self.hero_2.level)
        self.assertEqual(53, self.hero_2.health)
        self.assertEqual(15, self.hero_2.damage)
        self.assertEqual('You lose', result)

    def test_string_represent(self):
        result = str(self.hero)
        self.assertEqual('Hero Wizard: 10 lvl\nHealth: 77.7\nDamage: 15.2\n', result)


if __name__ == '__main__':
    main()
