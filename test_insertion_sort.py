import unittest
from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_regular_list(self):
        self.assertEqual(
            insertion_sort([5, 2, 4, 6, 1, 3]),
            [6, 5, 4, 3, 2, 1]
        )

    def test_already_decreasing(self):
        self.assertEqual(
            insertion_sort([9, 7, 5, 3, 1]),
            [9, 7, 5, 3, 1]
        )

    def test_increasing_list(self):
        self.assertEqual(
            insertion_sort([1, 2, 3, 4, 5]),
            [5, 4, 3, 2, 1]
        )

    def test_duplicate_values(self):
        self.assertEqual(
            insertion_sort([4, 2, 4, 1, 2]),
            [4, 4, 2, 2, 1]
        )

    def test_empty_list(self):
        self.assertEqual(insertion_sort([]), [])

    def test_single_element(self):
        self.assertEqual(insertion_sort([7]), [7])

    def test_negative_numbers(self):
        self.assertEqual(
            insertion_sort([-3, 5, -1, 0]),
            [5, 0, -1, -3]
        )


if __name__ == "__main__":
    unittest.main()