import unittest
import expected_value
import moda
import median
import most_frequent
from decimal import Decimal


class TestExpectedValue(unittest.TestCase):
    def test_result(self):
        values = [[1, 1, 1, 2, 2, 3, 3, 3, 3, 4], [1.5, 1.5, 1.5, 2.3, 2.3, 3.1, 3.1, 3.1, 3.1, 4.8]]
        results = [Decimal(2.3), Decimal(2.63)]
        for i in range(0, len(results)):
            results[i] = results[i].quantize(Decimal('.0001'))
        for value, result in zip(values, results):
            with self.subTest():
                self.assertEqual(expected_value.calculate_expected_value(value), result)


class TestModa(unittest.TestCase):
    def test_result(self):
        values = [[1, 1, 1, 2, 2, 3, 3, 3, 3, 4], [3.1, 1.5, 1.5, 2.3, 1.5, 3.1, 2.3, 3.1, 4.8]]
        results = [[3], [1.5, 3.1]]
        for value, result in zip(values, results):
            with self.subTest():
                self.assertCountEqual(moda.calculate_moda(value), result)


class TestMedian(unittest.TestCase):
    def test_result(self):
        values = [[1, 1, 1, 2, 2, 3, 3, 3, 3, 4], [1, 9, 4, 8, 5, 2, 3, 6, 7]]
        results = [2.5, 5]
        for value, result in zip(values, results):
            with self.subTest():
                self.assertEqual(median.median(value), result)


class TestMostFrequent(unittest.TestCase):
    def test_result(self):
        receipts = [[['item4', 'item5', 'item6', 'item1', 'item2', 'item7', 'item3'],
                    ['item5', 'item6', 'item7', 'item1', 'item4', 'item2', 'item3'],
                    ['item3', 'item5', 'item1', 'item4', 'item2', 'item6'],
                    ['item1', 'item6', 'item3', 'item2'],
                    ['item7', 'item5', 'item4', 'item2']],
                    [['item1', 'item2', 'item3', 'item5'],
                    ['item1', 'item2', 'item3', 'item4'],
                    ['item3', 'item4', 'item5'],
                    ['item3', 'item5', 'item6']]]
        results = [([{'item6', 'item2', 'item3', 'item1'}, {'item2', 'item4', 'item5'}], 4),
                   ([{'item3', 'item5'}], 3)]
        for receipt, result in zip(receipts, results):
            with self.subTest():
                self.assertCountEqual(most_frequent.most_frequent(receipt), result)


if __name__ == '__main__':
    unittest.main()
