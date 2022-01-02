class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if not self.__is_object_is_in(self.customers, customer):
            return
        self.__add_obj_to_list(self.customers, customer)

    def add_trainer(self, trainer):
        if not self.__is_object_is_in(self.trainers, trainer):
            return
        self.__add_obj_to_list(self.trainers, trainer)

    def add_equipment(self, equipment):
        if not self.__is_object_is_in(self.equipment, equipment):
            return
        self.__add_obj_to_list(self.equipment, equipment)

    def add_plan(self, plan):
        if not self.__is_object_is_in(self.plans, plan):
            return
        self.__add_obj_to_list(self.plans, plan)

    def add_subscription(self, subscription):
        if not self.__is_object_is_in(self.subscriptions, subscription):
            return
        self.__add_obj_to_list(self.subscriptions, subscription)

    def subscription_info(self, subscription_id):
        subscription = self.__get_object_by_id(self.subscriptions, subscription_id)
        customer = self.__get_object_by_id(self.customers, subscription.customer_id)
        trainer = self.__get_object_by_id(self.trainers, subscription.trainer_id)
        plan = self.__get_object_by_id(self.plans, subscription.exercise_id)
        equipment_id = plan.equipment_id
        equipment = self.__get_object_by_id(self.equipment, equipment_id)
        result = str(subscription) + '\n' + str(customer) + '\n' + str(trainer) + '\n' + str(equipment) + '\n' + str(plan)
        return result

    @staticmethod
    def __is_object_is_in(list_with_object, obj):
        if obj not in list_with_object:
            return True
        return False

    @staticmethod
    def __add_obj_to_list(list_to_add, obj):
        list_to_add.append(obj)
        return

    @staticmethod
    def __get_object_by_id(objects, current_id):
        for obj in objects:
            if obj.id == current_id:
                return obj
