stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 170
}

portfolio = {}
total_investment = 0

print("=== STOCK PORTFOLIO TRACKER ===")

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n--- Portfolio Summary ---")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value

    print(
        f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${value}"
    )

print(f"\nTotal Investment Value: ${total_investment}")

# Save to file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(
            f"{stock}: {quantity} shares x ${stock_prices[stock]} = ${value}\n"
        )

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("Portfolio saved to portfolio_summary.txt")

import os

print("\nFile saved at:")
print(os.path.abspath("portfolio_summary.txt"))
