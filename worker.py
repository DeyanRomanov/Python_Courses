class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Deyan', 1200, 10)

    def test_is_worker_initialed_correctly(self):
        self.assertEqual('Deyan', self.worker.name)
        self.assertEqual(1200, self.worker.salary)
        self.assertEqual(10, self.worker.energy)

    def test_if_energy_incremented_after_rest(self):
        self.worker.rest()
        self.assertEqual(11, self.worker.energy)

    def test_if_raise_error_if_tries_to_work_without_energy(self):
        self.worker = Worker('Deyan', 1200, 0)
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_if_workers_money_increased_by_his_salary(self):
        self.worker.work()
        self.assertEqual(1200, self.worker.money)

    def test_if_the_worker_energy_decreased_after_work(self):
        self.worker.work()
        self.assertEqual(9, self.worker.energy)

# •	Test if the get_info method returns the proper string with correct values
    def test_if_get_info_returns_the_proper_correct(self):
        self.worker.get_info()
        self.assertEqual('Deyan has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    unittest.main()
