import unittest
import phonebook


class TestPhonebook(unittest.TestCase):
    def test_create(self):
        pb = "phonebook.pb"
        self.assertEqual(phonebook.create(pb), "phonebook.pb has been created.")

    def test_add(self):
        pb = "phonebook.pb"
        name = "John Michael"
        number = '123 456 4323'

        self.assertEqual(phonebook.add(name, number, pb), "John Michael has been added to the phonebook.")

        name2 = "John Doe"
        number2 = "398 291 9281"

        self.assertEqual(phonebook.add(name2, number2, pb), "John Doe has been added to the phonebook.")

        self.assertEqual(phonebook.add(name, number, pb), "John Michael is already in the phonebook.")

    def test_lookup(self):
        pb = "phonebook.pb"
        name = "Sarah"
        self.assertEqual(phonebook.lookup(name, pb), "Sarah could not be found.")

        name2 = "John"

        self.test_add()
        self.assertEqual(phonebook.lookup(name2, pb), "John Michael 123 456 4323\nJohn Doe 398 291 9281\n")


if __name__ == '__main__':
    unittest.main()