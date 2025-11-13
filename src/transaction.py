
class Transaction:
    CURRENCY_SYMBOLS = {
        "USD": "$",
        "AUD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
        "INR": "₹"
    }

    def __init__(self, date, category, amount, currency, id=None):
        self.id = id
        self.amount = amount
        self.currency = currency
        self.date = date
        self.category = category

    def get_symbol(self):
        return self.CURRENCY_SYMBOLS.get(self.currency.upper(), self.currency)

    def __repr__(self):
        return f"Transaction('{self.date}', '{self.category}', {self.amount}, '{self.currency}')"

    def __str__(self):
        symbol = self.get_symbol()
        return f"| ID: {self.id} | Date: {self.date} | Category: {self.category} | Amount: {symbol}{self.amount:.2f} |"