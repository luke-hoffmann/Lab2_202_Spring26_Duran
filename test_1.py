import unittest

from lab2_1 import recursive_search
class TestSearchFunction(unittest.TestCase):

    # 1. Standard placement cases
    def test_target_in_middle(self):
        self.assertEqual(recursive_search([10, 20, 30, 40, 50], target=30), 2)

    def test_target_at_beginning(self):
        self.assertEqual(recursive_search([1, 2, 3, 4, 5], target=1), 0)

    def test_target_at_end(self):
        self.assertEqual(recursive_search([1, 2, 3, 4, 5], target=5), 4)

    # 2. Missing target
    def test_target_not_found(self):
        self.assertEqual(recursive_search([10, 20, 30], target=99), -1)

if __name__ == '__main__':
    unittest.main()
