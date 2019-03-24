from Content import Content
import unittest
from unittest import TestCase, mock

class TestSaod(unittest.TestCase):
    def test_start(self):
        content = Content("Test", 10)
        self.assertEqual("Test", content._name)

    def test_size(self):
        content = Content("Test", 10)
        self.assertEqual(10, content._size)

    def test_sec(self):
        content = Content("Test", 10)
        self.assertEqual(None, content._section)

    def test_add_worker(self):
        content = Content("Test", 10)
        with mock.patch('__builtin__.input', side_effect = ['ttt']):
            content.Add_section()
        self.assertEqual(1, content._count)

if __name__ == '__main__':
    unittest.main()