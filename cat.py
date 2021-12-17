class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):

    def setUp(self):
        self.cat = Cat('tom')

    def test_if_increased_after_eating(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_if_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_raise_if_cat_is_already_fed_and_eat(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_raise_cat_cannot_asleep_if_not_feed(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
