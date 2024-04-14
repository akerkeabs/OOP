class StockInfo:
    def __init__(self, company, country, price, currency):
        self.company = company
        self.country = country
        self.price = price
        self.currency = currency

    def __str__(self):
        return f"Company: {self.company}\nCountry: {self.country}\nPrice: {self.currency} {self.price}"

stock = StockInfo("Apple Inc.", "USA", 150, "USD")
print(stock)