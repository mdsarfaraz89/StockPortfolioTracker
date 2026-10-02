import csv
import os
import tempfile
import unittest
from stock_tracker import calculate, save_csv, STOCK_PRICES


class TestStockTracker(unittest.TestCase):
    def test_calculate_total(self):
        rows, total = calculate({"AAPL": 10, "TSLA": 5})
        self.assertEqual(total, 10 * STOCK_PRICES["AAPL"] + 5 * STOCK_PRICES["TSLA"])
        self.assertEqual(len(rows), 2)

    def test_calculate_empty(self):
        rows, total = calculate({})
        self.assertEqual((rows, total), ([], 0))

    def test_save_csv(self):
        rows, total = calculate({"MSFT": 2})
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "out.csv")
            save_csv(rows, total, path)
            with open(path, newline="") as f:
                content = list(csv.reader(f))
        self.assertEqual(content[0], ["Stock", "Quantity", "Price", "Value"])
        self.assertEqual(content[1], ["MSFT", "2", "330", "660"])


if __name__ == "__main__":
    unittest.main()
