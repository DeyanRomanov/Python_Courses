class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class ListTests(TestCase):
    def setUp(self):
        self.list_integer = IntegerList(1, 2, 3)

    def test_if_is_initialed_correctly(self):
        list_integer = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], self.list_integer._IntegerList__data)

    def test_add_operation_add_and_returns(self):
        self.list_integer.add(4)
        self.assertEqual([1, 2, 3, 4], self.list_integer._IntegerList__data)

    def test_element_if_float_thrown_error(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integer.add(5.6)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_element_if_str_thrown_error(self):
        with self.assertRaises(ValueError) as ex:
            self.list_integer.add("8")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_take_only_integer_in_initialed(self):
        self.list_integer = IntegerList(4.6, "8", 1)
        self.assertEqual([1], self.list_integer._IntegerList__data)

    def test_remove_element_on_that_index_otherwise_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integer.remove_index(8)
        self.assertEqual("Index is out of range", str(ex.exception))
        element = self.list_integer.remove_index(0)
        self.assertEqual(1, element)

    def test_get_element_on_that_index_otherwise_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integer.get(100)
        self.assertEqual("Index is out of range", str(ex.exception))
        element = self.list_integer.get(0)
        self.assertEqual(1, element)

    def test_insert_element_to_index_if_not_valid_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.list_integer.insert(10, 1)
        self.assertEqual("Index is out of range", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.list_integer.insert(1, "6")
        self.assertEqual("Element is not Integer", str(ex.exception))
        self.list_integer.insert(2, 4)
        self.assertEqual([1, 2, 4, 3], self.list_integer._IntegerList__data)

    def test_if_get_biggest_return_biggest_element(self):
        element = self.list_integer.get_biggest()
        self.assertEqual(3, element)

    def test_get_index_by_element(self):
        index = self.list_integer.get_index(2)
        self.assertEqual(1, index)

if __name__ == '__main__':
    main()