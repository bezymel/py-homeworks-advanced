import unittest
from app import add_new_doc, delete_doc, get_all_doc_owners_names


class TestAppFunctions(unittest.TestCase):

    def test_add_new_doc(self):
        add_new_doc('insurance', '123456789', 'Иван Петров', '4')
        self.assertTrue(check_document_existance('123456789'))

    def test_delete_doc(self):
        delete_doc('11-2')
        self.assertFalse(check_document_existance('11-2'))

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), ['Василий Гупкин', 'Геннадий Покемонов'])

if __name__ == '__main__':
    unittest.main()
