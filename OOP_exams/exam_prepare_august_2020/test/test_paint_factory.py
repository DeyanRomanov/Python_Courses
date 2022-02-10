from unittest import main, TestCase

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.factory = PaintFactory('Megahim', 5)
        self.valid_ingredients = ["white", "yellow", "blue", "green", "red"]

    def test_initialization(self):
        self.assertEqual('Megahim', self.factory.name)
        self.assertEqual(5, self.factory.capacity)

    def test_add_ingredient(self):
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient("white", 6)
        self.assertEqual("Not enough space in factory", str(ex.exception))
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient("asd", 6)
        self.assertEqual("Ingredient of type asd not allowed in PaintFactory", str(ex.exception))
        self.factory.ingredients = {'white': 3}
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient("white", 3)
        self.assertEqual("Not enough space in factory", str(ex.exception))
        self.factory.add_ingredient("white", 2)
        self.assertEqual({'white': 5}, self.factory.ingredients)

    def test_can_add(self):
        self.assertEqual(False, self.factory.can_add(10))
        self.assertEqual(True, self.factory.can_add(5))
        self.factory.ingredients = {'white': 3, 'yellow': 2}
        self.assertEqual(False, self.factory.can_add(1))

    def test_represent(self):
        self.factory.ingredients = {'white': 3, 'yellow': 2}
        result = f"Factory name: Megahim with capacity 5.\nwhite: 3\nyellow: 2\n"
        self.assertEqual(result, self.factory.__repr__())

    def test_remove_ingredient(self):
        self.factory.ingredients = {'white': 3}
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient("white", 6)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient("asd", 6)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))
        self.factory.remove_ingredient('white', 3)
        self.assertEqual({'white': 0}, self.factory.ingredients)

    def test_products(self):
        self.factory.ingredients = {'white': 3}
        self.assertEqual({'white': 3}, self.factory.products)

    if __name__ == '__main__':
        main()
