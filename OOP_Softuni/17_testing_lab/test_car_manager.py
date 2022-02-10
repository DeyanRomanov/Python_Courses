# from 17_testing_lab.car_manager import Car

from unittest import TestCase, main


class CarTests(TestCase):
    def setUp(self):
        self.car = Car('audi', 'a4', 8, 70)

    def test_initialed_car(self):
        self.assertEqual('audi', self.car.make)
        self.assertEqual('a4', self.car.model)
        self.assertEqual(8, self.car.fuel_consumption)
        self.assertEqual(70, self.car.fuel_capacity)

    def test_make_length_raise_if_is_none(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_length_raise_if_is_none(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_negative_or_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_negative_or_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_raise_if_is_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_if_is_negative_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_if_refuel_amount_is_greater_than_capacity(self):
        self.car.fuel_amount = 5
        self.car.fuel_capacity = 6
        self.car.refuel(5)
        self.assertEqual(6, self.car.fuel_amount)

    def test_drive_distance_raise_not_have_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_whit_enough_fuel(self):
        self.car.fuel_amount = 20
        self.car.drive(50)
        self.assertEqual(16, self.car.fuel_amount)


if __name__ == "__main__":
    main()
