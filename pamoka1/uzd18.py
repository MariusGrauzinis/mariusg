class Currency:
    def __init__(self, code="USD", amount=0.0, rate=1.0):
        self.code = code
        self.amount = amount
        self.rate = rate

    def set_code(self, code): self.code = code; return self
    def set_amount(self, amount): self.amount = amount; return self
    def set_exchange_rate(self, rate): self.rate = rate; return self

    def convert(self, new_code, new_rate):
        self.amount = self.amount / self.rate * new_rate
        self.code = new_code
        self.rate = new_rate
        return self

    def __str__(self):
        return f"{self.code}: {self.amount:.2f}"
    
val = Currency().set_code("EUR").set_amount(100).set_exchange_rate(0.9)
print(val)

val.convert("USD", 1.0)
print(val)