
class BankAccount:
    bank_name: str = "SEB"
    all_accounts: list["BankAccount"] = []

    def __init__(self, owner: str, balance: float = 0) -> None:
        self.owner = owner
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount: float) -> str:
        self.balance += amount
        return f"{self.owner} deposited {amount}. New balance: {self.balance}"

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name

    @classmethod
    def create_with_bonus(cls, owner: str, bonus: float) -> "BankAccount":
        return cls(owner, balance=bonus)

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        return amount > 0







acc1 = BankAccount("Jonas", 1000.0)   
acc2 = BankAccount.create_with_bonus("Milda", 50) 

print(acc1.deposit(2250))  
print(BankAccount.get_bank_name()) 
print(BankAccount.is_valid_amount(10)) 




