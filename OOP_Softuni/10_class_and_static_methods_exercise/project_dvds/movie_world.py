from project_storage.customer import Customer
from project_storage.dvd import DVD


class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []
        self.dvd_capacities = 0
        self.customers_capacity = 0

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if self.customer_capacity() > self.customers_capacity:
            self.customers_capacity += 1
            self.customers.append(customer)
            return

    def add_dvd(self, dvd):
        if self.dvd_capacity() > self.dvd_capacities:
            self.dvd_capacities += 1
            self.dvds.append(dvd)
            return

    def rent_dvd(self, customer_id, dvd_id):
        client = self.__get_obj_by_id(self.customers, customer_id)
        dvd = self.__get_obj_by_id(self.dvds, dvd_id)
        if dvd in client.rented_dvds:
            return f"{client.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return "DVD is already rented"
        elif client.age < dvd.age_restriction:
            return f"{client.name} should be at least {dvd.age_restriction} to rent this movie"
        client.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{client.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        client = self.__get_obj_by_id(self.customers, customer_id)
        dvd = self.__get_obj_by_id(self.dvds, dvd_id)
        if dvd not in client.rented_dvds:
            return f"{client.name} does not have that DVD"
        client.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{client.name} has successfully returned {dvd.name}"

    def __get_obj_by_id(self, objects, ids):
        for obj in objects:
            if obj.id == ids:
                return obj

    def __repr__(self):
        client = '\n'.join([str(c) for c in self.customers])
        dvd = '\n'.join([str(d) for d in self.dvds])
        result = client + '\n' + dvd
        return result

