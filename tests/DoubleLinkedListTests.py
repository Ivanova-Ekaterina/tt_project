from app.DoubleLinkedList import DoubleLinkedList
import unittest


class TestMyFunc(unittest.TestCase):
    def test_push_pop(self):
        test_list = DoubleLinkedList()
        test_list.push(5)
        self.assertEqual(test_list.len(), 1)
        self.assertEqual(test_list.pop(), 5)

    def test_pop_empty(self):
        test_list = DoubleLinkedList()
        self.assertEqual(test_list.pop(), "list is empty")

    def test_pop(self):
        test_list = DoubleLinkedList()
        for i in range(5):
            test_list.push(i)
        for i in range(5):
            self.assertEqual(test_list.pop(), 4 - i)

    def test_push(self):
        test_list = DoubleLinkedList()
        test_list.push(1)
        test_list.push("test")
        test_list.push(3.2)
        self.assertEqual(test_list.len(), 3)
        self.assertEqual(test_list.show(), [1, "test", 3.2])

    def test_unshift(self):
        test_list = DoubleLinkedList()
        test_list.unshift(1)
        test_list.unshift("test")
        test_list.unshift(3.2)
        self.assertEqual(test_list.len(), 3)
        self.assertEqual(test_list.show(), [3.2, "test", 1])

    def test_unshift_shift(self):
        test_list = DoubleLinkedList()
        test_list.unshift(5)
        self.assertEqual(test_list.len(), 1)
        self.assertEqual(test_list.shift(), 5)

    def test_shift_empty(self):
        test_list = DoubleLinkedList()
        self.assertEqual(test_list.shift(), "list is empty")

    def test_shift(self):
        test_list = DoubleLinkedList()
        for i in range(5):
            test_list.push(i)
        for i in range(5):
            self.assertEqual(test_list.shift(), i)

    def test_len_empty(self):
        test_list = DoubleLinkedList()
        self.assertEqual(test_list.len(), 0)

    def test_len(self):
        test_list = DoubleLinkedList()
        for i in range(10):
            test_list.push(i)
        self.assertEqual(test_list.len(), 10)

    def test_contains_empty(self):
        test_list = DoubleLinkedList()
        self.assertEqual(test_list.contains("test"), 0)

    def test_contains_only_elem(self):
        test_list = DoubleLinkedList()
        test_list.push("test")
        self.assertEqual(test_list.len(), 1)
        self.assertEqual(test_list.contains("test"), 1)

    def test_contains_only_multi_elem(self):
        test_list = DoubleLinkedList()
        for i in range(10):
            test_list.push(1)
        self.assertEqual(test_list.len(), 10)
        self.assertEqual(test_list.contains(1), 10)

    def test_contains_elem(self):
        test_list = DoubleLinkedList()
        for i in range(10):
            test_list.push(i)
        self.assertEqual(test_list.len(), 10)
        self.assertEqual(test_list.contains(4), 1)

    def test_not_contains_elem(self):
        test_list = DoubleLinkedList()
        for i in range(10):
            test_list.push(i)
        self.assertEqual(test_list.len(), 10)
        self.assertEqual(test_list.contains(14), 0)

    def test_contains_multi_elem(self):
        test_list = DoubleLinkedList()
        for i in range(10):
            test_list.push(i)
        for i in range(3):
            test_list.push(5)
        self.assertEqual(test_list.len(), 13)
        self.assertEqual(test_list.contains(5), 4)

    def test_delete_empty(self):
        test_list = DoubleLinkedList()
        self.assertEqual(test_list.delete("test"), "no such element")

    def test_delete_elem_only(self):
        test_list = DoubleLinkedList()
        test_list.push("test")
        self.assertEqual(test_list.len(), 1)
        test_list.delete("test")
        self.assertEqual(test_list.len(), 0)

    def test_delete_elem(self):
        test_list = DoubleLinkedList()
        for i in range(5):
            test_list.push(i)
        self.assertEqual(test_list.len(), 5)
        self.assertEqual(test_list.contains(2), 1)
        test_list.delete(2)
        self.assertEqual(test_list.len(), 4)
        self.assertEqual(test_list.contains(2), 0)

    def test_delete_elem_only_multi(self):
        test_list = DoubleLinkedList()
        for i in range(5):
            test_list.push(2)
        self.assertEqual(test_list.len(), 5)
        self.assertEqual(test_list.contains(2), 5)
        test_list.delete(2)
        self.assertEqual(test_list.len(), 0)
        self.assertEqual(test_list.contains(2), 0)

    def test_delete_elem_multi(self):
        test_list = DoubleLinkedList()
        for i in range(3):
            test_list.push(i)
        test_list.push(1)
        for i in range(3):
            test_list.push(i)
        self.assertEqual(test_list.len(), 7)
        self.assertEqual(test_list.contains(1), 3)
        test_list.delete(1)
        self.assertEqual(test_list.len(), 4)
        self.assertEqual(test_list.contains(1), 0)

    def test_first_empty(self):
        test_list = DoubleLinkedList()
        self.assertEqual(test_list.first(), "list is empty")

    def test_first(self):
        test_list = DoubleLinkedList()
        for i in range(5):
            test_list.push(i)
        self.assertEqual(test_list.first(), 0)
        self.assertEqual(test_list.len(), 5)

    def test_first_only(self):
        test_list = DoubleLinkedList()
        test_list.push("test")
        self.assertEqual(test_list.first(), "test")

    def test_last_empty(self):
        test_list = DoubleLinkedList()
        self.assertEqual(test_list.last(), "list is empty")

    def test_last(self):
        test_list = DoubleLinkedList()
        for i in range(5):
            test_list.push(i)
        self.assertEqual(test_list.last(), 4)
        self.assertEqual(test_list.len(), 5)

    def test_last_only(self):
        test_list = DoubleLinkedList()
        test_list.push("test")
        self.assertEqual(test_list.last(), "test")
