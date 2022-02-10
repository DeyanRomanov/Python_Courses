from exam_prepare_august_2021.project import Student

from unittest import TestCase, main


class StudentTests(TestCase):
    def setUp(self):
        self.student = Student('Dido', {'course_name': ['notes']})

    def test_initialed_correctly(self):
        self.assertEqual('Dido', self.student.name)
        self.assertEqual({'course_name': ['notes']}, self.student.courses)

    def test_initialed_correctly_without_courses(self):
        self.student = Student('Dido')
        self.assertEqual({}, self.student.courses)

    def test_enroll_if_course_is_already_added(self):
        result = self.student.enroll('course_name', ['notes2', 'notes3'], 'asd')
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({'course_name': ['notes', 'notes2', 'notes3']}, self.student.courses)

    def test_enroll_if_course_not_already_added_without_course_note(self):
        result = self.student.enroll('course_name2', ['notes2', 'notes3'], '')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(['notes2', 'notes3'], self.student.courses['course_name2'])
        self.assertTrue('course_name2' in self.student.courses)

    def test_enroll_if_course_not_already_added_with_course_note(self):
        result = self.student.enroll('course_name2', ['notes2', 'notes3'], 'Y')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(['notes2', 'notes3'], self.student.courses['course_name2'])
        self.assertTrue('course_name2' in self.student.courses)

    def test_enroll_if_course_not_added_and_is_empty(self):
        result = self.student.enroll('course_name2', [1, 2], 'No')
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses['course_name2'])
        self.assertTrue('course_name2' in self.student.courses)

    def test_add_notes_raise_if_course_not_added(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('math', [5, 6, 8])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_course_is_added(self):
        result = self.student.add_notes('course_name', 8)
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['notes', 8], self.student.courses['course_name'])

    def test_raise_try_to_leave_not_added_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('math')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_added_course(self):
        self.student = Student('Dido', {'course_name': ['notes'], 'math': [8, 8, 9]})
        result = self.student.leave_course('math')
        self.assertEqual("Course has been removed", result)
        self.assertEqual({'course_name': ['notes']}, self.student.courses)


if __name__ == '__main__':
    main()
