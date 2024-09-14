import unittest

import DynamicArray 

class TestDynamicArray(unittest.TestCase):
    def setUp(self):
        self.dyn_array = DynamicArray()

    def test_initial_capacity(self):
        self.assertEqual(self.dyn_array.capacity, 16)

    def test_size(self):
        self.assertEqual(self.dyn_array.size(), 0)

    def test_is_empty(self):
        self.assertTrue(self.dyn_array.is_empty())
        self.dyn_array.append(10)
        self.assertFalse(self.dyn_array.is_empty())

    def test_append(self):
        self.dyn_array.append(10)
        self.assertEqual(self.dyn_array.get(0), 10)
        self.assertEqual(self.dyn_array.size(), 1)

    def test_get(self):
        self.dyn_array.append(10)
        self.dyn_array.append(20)
        self.assertEqual(self.dyn_array.get(1), 20)
        with self.assertRaises(IndexError):
            self.dyn_array.get(3)

    def test_set(self):
        self.dyn_array.append(10)
        self.dyn_array.set(0, 15)
        self.assertEqual(self.dyn_array.get(0), 15)

    def test_clear(self):
        self.dyn_array.append(10)
        self.dyn_array.append(20)
        self.dyn_array.clear()
        self.assertEqual(self.dyn_array.size(), 0)
        self.assertTrue(self.dyn_array.is_empty())

    def test_add(self):
        self.dyn_array.append(10)
        self.dyn_array.append(20)
        self.dyn_array.add(1, 15)
        self.assertEqual(self.dyn_array.get(1), 15)
        self.assertEqual(self.dyn_array.size(), 3)

    def test_remove(self):
        self.dyn_array.append(10)
        self.dyn_array.append(20)
        removed = self.dyn_array.remove(0)
        self.assertEqual(removed, 10)
        self.assertEqual(self.dyn_array.size(), 1)

    def test_index_of(self):
        self.dyn_array.append(10)
        self.dyn_array.append(20)
        self.assertEqual(self.dyn_array.index_of(20), 1)
        self.assertEqual(self.dyn_array.index_of(30), -1)

    def test_contains(self):
        self.dyn_array.append(10)
        self.assertTrue(self.dyn_array.contains(10))
        self.assertFalse(self.dyn_array.contains(20))

    def test_insertion_sort(self):
        self.dyn_array.append(30)
        self.dyn_array.append(10)
        self.dyn_array.append(20)
        self.dyn_array.InsertionSort()
        self.assertEqual(str(self.dyn_array), "[10,20,30]")

    def test_selection_sort(self):
        self.dyn_array.append(30)
        self.dyn_array.append(10)
        self.dyn_array.append(20)
        self.dyn_array.SelectionSort()
        self.assertEqual(str(self.dyn_array), "[30,20,10]")

    def test_bubble_sort(self):
        self.dyn_array.append(30)
        self.dyn_array.append(10)
        self.dyn_array.append(20)
        self.dyn_array.BubbleSort()
        self.assertEqual(str(self.dyn_array), "[30,20,10]")

    def test_iter(self):
        self.dyn_array.append(10)
        self.dyn_array.append(20)
        iter_array = list(iter(self.dyn_array))
        self.assertEqual(iter_array, [10, 20])

if __name__ == '__main__':
    unittest.main()
