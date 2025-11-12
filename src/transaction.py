
class Transaction:
    CURRENCY_SYMBOLS = {
        "USD": "$",
        "AUD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
        "INR": "₹"
    }

    def __init__(self, amount, currency, date, category, id=None):
        self.id = id
        self.amount = amount
        self.currency = currency
        self.date = date
        self.category = category

    def get_symbol(self):
        return self.CURRENCY_SYMBOLS.get(self.currency.upper(), self.currency)

    def __repr__(self):
        return f"Transaction('{self.amount}', '{self.currency}', {self.amount}, '{self.date}')"

    def __str__(self):
        symbol = self.get_symbol()
        return f"{self.date}: {self.category} - {symbol}{self.amount:.2f}"