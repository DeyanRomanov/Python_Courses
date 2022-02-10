from exam_prepare_august_2021.project3.library import Library
from unittest import TestCase, main


class LibraryTest(TestCase):
    def setUp(self):
        self.library = Library('Lyuben Karavelov')

    def test_initialised_with_correct_len(self):
        self.assertEqual('Lyuben Karavelov', self.library.name)

    def test_if_name_is_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.library = Library('')
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book(self):
        self.library.add_book('ivan vazov', 'pod igoto')
        self.assertEqual({'ivan vazov': ["pod igoto"]}, self.library.books_by_authors)

    def test_add_book_if_author_is_added(self):
        self.library.books_by_authors = {'ivan vazov': []}
        self.library.add_book('ivan vazov', 'pod igoto')
        self.assertEqual({'ivan vazov': ["pod igoto"]}, self.library.books_by_authors)

    def test_add_bool_if_title_in_authot_list(self):
        self.library.books_by_authors = {'ivan vazov': ['pod igoto']}
        self.library.add_book('ivan vazov', 'pod igoto')
        self.assertEqual({'ivan vazov': ["pod igoto"]}, self.library.books_by_authors)

    def test_add_reader_if_reader_already_is_added(self):
        self.library.readers = {'dido': []}
        self.assertEqual('dido is already registered in the Lyuben Karavelov library.', self.library.add_reader('dido'))

    def test_add_reader(self):
        self.library.add_reader({'dido': []})
        self.assertEqual({'dido': []}, self.library.readers)

    def test_rent_book_if_name_not_in_readers(self):
        result = self.library.rent_book('dido', 'ivan vazov', 'pod igoto')
        self.assertEqual('dido is not registered in the Lyuben Karavelov Library.', result)

    def test_if_book_author_not_in_authors(self):
        self.library.readers = {'dido': []}
        result = self.library.rent_book('dido', 'ivan vazov', 'pod igoto')
        self.assertEqual("Lyuben Karavelov Library does not have any ivan vazov's books.", result)

    def test_if_book_title_not_in_book_authors_dict(self):
        self.library.readers = {'dido': []}
        self.library.books_by_authors = {'ivan vazov': ['glad']}
        result = self.library.rent_book('dido', 'ivan vazov', 'pod igoto')
        self.assertEqual("""Lyuben Karavelov Library does not have ivan vazov's "pod igoto".""", result)

    def test_if_rent_book(self):
        self.library.readers = {'dido': []}
        self.library.books_by_authors = {'ivan vazov': ['glad']}
        self.library.rent_book('dido', 'ivan vazov', 'glad')
        self.assertEqual([{'ivan vazov': 'glad'}], self.library.readers['dido'])
        self.assertEqual({'ivan vazov': []}, self.library.books_by_authors)


if __name__ == '__main__':
    main()
