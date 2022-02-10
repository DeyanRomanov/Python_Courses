from unittest import TestCase, main
from pet_shop import PetShop


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop("shop")

    def test_initialisation(self):
        self.shop.food = {'bread': 15.5}
        self.shop.pets = ['dog', 'cat']

        self.assertEqual('shop', self.shop.name)
        self.assertEqual({'bread': 15.5}, self.shop.food)
        self.assertEqual(['dog', 'cat'], self.shop.pets)

    def test_add_food(self):
        result = self.shop.add_food('bread', 15.5)
        self.assertEqual(f"Successfully added 15.50 grams of bread.", result)
        self.assertEqual({'bread': 15.5}, self.shop.food)

    def test_add_food_raise_if_quantity_equal_or_less_to_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.shop.add_food('bread', -0.1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))
        self.assertEqual({}, self.shop.food)

    def test_if_food_is_there_increase_quantity(self):
        self.shop.food = {'bread': 15.5}
        result = self.shop.add_food('bread', 2.5)
        self.assertEqual(f"Successfully added 2.50 grams of bread.", result)
        self.assertEqual({'bread': 18}, self.shop.food)

    def test_add_pet(self):
        result = self.shop.add_pet('duck')
        self.assertEqual(f"Successfully added duck.", result)
        self.assertEqual(['duck'], self.shop.pets)

    def test_raise_error_if_pet_is_already_in_shop(self):
        self.shop.pets = ['dog', 'cat']
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet('dog')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual(['dog', 'cat'], self.shop.pets)

    def test_raise_error_if_pet_not_in_shop_feed_pet(self):
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet('bread', 'duck')
        self.assertEqual(f"Please insert a valid pet name", str(ex.exception))

    def test_return_message_if_food_not_in_menu(self):
        self.shop.pets = ['duck']
        result = self.shop.feed_pet('bread', 'duck')
        self.assertEqual('You do not have bread', result)

    def test_if_feed_pets_and_food_is_less_than_100(self):
        self.shop.food = {'bread': 15.5}
        self.shop.pets = ['duck']
        result = self.shop.feed_pet('bread', 'duck')
        self.assertEqual("Adding food...", result)
        self.assertEqual({'bread': 1015.50}, self.shop.food)

    def test_if_everything_is_ok(self):
        self.shop.food = {'bread': 215.5}
        self.shop.pets = ['duck']
        result = self.shop.feed_pet('bread', 'duck')
        self.assertEqual("duck was successfully fed", result)
        self.assertEqual({'bread': 115.5}, self.shop.food)

    def test_represent(self):
        self.shop.pets = ['dog', 'cat']
        self.assertEqual(f'Shop shop:\nPets: dog, cat', self.shop.__repr__())


if __name__ == '__main__':
    main()
