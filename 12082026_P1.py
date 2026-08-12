from dataclasses import dataclass

@dataclass
class StockPosition:
    ticker: str
    shares: int
    avg_cost: float

    # A simple method to calculate position value
    def current_value(self, market_price: float) -> float:
        return self.shares * market_price

# 1. Instantiating data objects is clean and easy
pos1 = StockPosition("AAPL", 50, 150.00)
pos2 = StockPosition("TSLA", 10, 250.00)

# 2. Automatic __repr__ makes logging and printing instantly readable
print("Current Portfolio:")
print(pos1)  # Outputs: StockPosition(ticker='AAPL', shares=50, avg_cost=150.0)
print(pos2)  # Outputs: StockPosition(ticker='TSLA', shares=10, avg_cost=250.0)

# 3. Automatic __eq__ makes structural equality comparisons work out of the box
pos3 = StockPosition("AAPL", 50, 150.00)
print("\nIs pos1 identical to pos3?")
print(pos1 == pos3)  # Outputs: True (because all field values match)

# 4. Using class methods just like a normal class
current_aapl_price = 175.50
print(f"\nValue of AAPL Position: ${pos1.current_value(current_aapl_price)}")
