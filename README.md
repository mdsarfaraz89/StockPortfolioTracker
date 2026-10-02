# CodeAlpha_StockPortfolioTracker

A console tool that calculates your total investment from stock names and quantities, and saves the result to a CSV file.

> Built for the **CodeAlpha Python Programming Internship**.

## Features
- Hardcoded dictionary of stock prices
- Add as many stocks as you like; repeated entries are added together
- Input validation for unknown symbols and bad quantities
- Per-stock value and total investment
- Saves a report to `portfolio.csv`
- Unit tests

## Concepts used
- Dictionaries
- `input()` / `print()` and type conversion
- `try` / `except`
- Functions
- File handling with the `csv` module
- `unittest`

## Project structure
```
CodeAlpha_StockPortfolioTracker/
+-- stock_tracker.py
+-- test_stock_tracker.py
+-- StockPortfolioTracker.ipynb
+-- README.md
+-- requirements.txt
+-- .gitignore
```

## How to run
Requires Python 3.8+ (no external libraries).

```bash
python stock_tracker.py
```

Run the unit tests:
```bash
python -m unittest -v
```

Open the step-by-step notebook:
```bash
pip install jupyter
jupyter notebook
```

## Sample run
```
Available stocks:
  AAPL: $180
  TSLA: $250
  ...

Stock symbol (or 'done'): aapl
Quantity of AAPL: 10

Stock symbol (or 'done'): tsla
Quantity of TSLA: 5

Stock symbol (or 'done'): done

--- Portfolio Summary ---
AAPL: 10 x $180 = $1800
TSLA: 5 x $250 = $1250
Total investment: $3050
Saved to portfolio.csv
```

## Future improvements
- Menu to view, add and remove holdings
- Percentage allocation per stock
- Fetch live prices from an API
- Plot the allocation with matplotlib

## Author
Your Name - [LinkedIn](https://linkedin.com/in/your-profile) - [GitHub](https://github.com/your-username)
