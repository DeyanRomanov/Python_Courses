from exam_prepare_august_2021.project import Vehicle

from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(55.5, 140)

    def test_initialise(self):
        self.assertEqual(55.5, self.vehicle.fuel)
        self.assertEqual(55.5, self.vehicle.capacity)
        self.assertEqual(140, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_raise_if_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100000)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_drive_if_fuel_is_enough(self):
        self.vehicle.drive(10)
        self.assertEqual(43, self.vehicle.fuel)

    def test_refuel_raise_error_if_is_too_much(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_if_have_capacity(self):
        self.vehicle.fuel = 10
        self.vehicle.capacity = 40
        self.vehicle.refuel(20)
        self.assertEqual(30, self.vehicle.fuel)

    def test_for_str_represent(self):
        result = self.vehicle.__str__()
        self.assertEqual("The vehicle has 140 horse power with 55.5 fuel left and 1.25 fuel consumption", result)


if __name__ == "__main__":
    main()
