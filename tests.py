import unittest
from quicksort import QuickSort
import random

class TestSort(unittest.TestCase):
    def test_quicksort(self):
        quicksort = QuickSort()
        for i in range(1000, 2000):
            lst = [random.randint(0, 500) for _ in range(i)]
            ground_truth = sorted(lst)
            quicksort.sort(lst)
            self.assertEqual(ground_truth, lst)

if __name__ == '__main__':
    unittest.main()