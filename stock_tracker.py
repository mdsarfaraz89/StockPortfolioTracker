"""Calculate total investment from hardcoded stock prices.

CodeAlpha Python Programming Internship.
"""

import csv
from datetime import datetime

STOCK_PRICES = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 330, "AMZN": 135}


def show_available_stocks():
    print("\nAvailable stocks:")
    for symbol, price in STOCK_PRICES.items():
        print("  " + symbol + ": $" + str(price))


def get_portfolio():
    portfolio = {}
    while True:
        symbol = input("\nStock symbol (or 'done'): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Unknown stock. Please choose from the list.")
            continue
        try:
            qty = int(input("Quantity of " + symbol + ": "))
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("Please enter a positive whole number.")
            continue
        portfolio[symbol] = portfolio.get(symbol, 0) + qty
    return portfolio


def calculate(portfolio):
    """Return (rows, total). Each row is [symbol, quantity, price, value]."""
    rows = []
    total = 0
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        rows.append([symbol, qty, price, value])
    return rows, total


def print_summary(rows, total):
    print("\n--- Portfolio Summary ---")
    for symbol, qty, price, value in rows:
        print(symbol + ": " + str(qty) + " x $" + str(price) + " = $" + str(value))
    print("Total investment: $" + str(total))


def save_csv(rows, total, filename="portfolio.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        writer.writerows(rows)
        writer.writerow([])
        writer.writerow(["Total", "", "", total])
        writer.writerow(["Generated", datetime.now().strftime("%Y-%m-%d %H:%M")])
    print("Saved to " + filename)


def main():
    show_available_stocks()
    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered.")
        return
    rows, total = calculate(portfolio)
    print_summary(rows, total)
    save_csv(rows, total)


if __name__ == "__main__":
    main()
