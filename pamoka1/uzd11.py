class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance  
        

    def deposit(self, amount: int) -> None:
        
        if amount > 0:
            self._balance += amount
            print(f"Money put to account: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: int) -> None:
      
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Successfully withdrawn: ${amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self) -> str:
        return f"Current Balance: ${self._balance}"

    

account = BankAccount(1000.0)
account.deposit(190.0)
account.withdraw(250.0)
print(account.check_balance())